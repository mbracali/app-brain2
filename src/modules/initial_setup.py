"""
Cross-platform bootstrap for user config at ~/.brain2/brain2_config.toml.

Public access pattern:
- Call initialize_app_config() once at app startup.
- Import and call get_app_config() anywhere else in the app.
"""

from __future__ import annotations

from dataclasses import dataclass
import ctypes
from pathlib import Path
from typing import Any
import tomllib

_CONFIG_DIR_NAME = ".brain2"
_CONFIG_FILE_NAME = "brain2_config.toml"
_DEFAULT_CONFIG_HEADER = "# Brain2 user config\n"
_APP_CONFIG: dict[str, Any] | None = None


@dataclass(frozen=True)
class Brain2Paths:
    """Resolved per-user paths used by app bootstrap."""

    home_dir: Path
    config_dir: Path
    config_file: Path


class ConfigParseError(ValueError):
    """Raised when brain2_config.toml is present but invalid TOML."""


@dataclass(frozen=True)
class BrainRecord:
    """Persisted brain entry."""

    brain_name: str
    categories: list[str]
    root_folder: str
    create_named_folder: bool


def get_brain2_paths() -> Brain2Paths:
    """Return cross-platform user paths for config directory and file."""
    home_dir = Path.home()
    config_dir = home_dir / _CONFIG_DIR_NAME
    config_file = config_dir / _CONFIG_FILE_NAME
    return Brain2Paths(home_dir=home_dir, config_dir=config_dir, config_file=config_file)


def _hide_directory_on_windows(directory: Path) -> None:
    """Set hidden attribute on Windows for dot-folder parity."""
    if not directory.exists() or directory.name != _CONFIG_DIR_NAME:
        return
    if not hasattr(ctypes, "windll"):
        return

    file_attribute_hidden = 0x02
    set_file_attributes = ctypes.windll.kernel32.SetFileAttributesW
    result = set_file_attributes(str(directory), file_attribute_hidden)
    if result == 0:
        raise PermissionError(f"Unable to mark directory as hidden: {directory}")


def ensure_user_config_file() -> Path:
    """Create ~/.brain2 and brain2_config.toml if missing, then return the file path."""
    paths = get_brain2_paths()
    try:
        paths.config_dir.mkdir(parents=True, exist_ok=True)
        if paths.config_dir.exists() and paths.config_dir.is_dir():
            _hide_directory_on_windows(paths.config_dir)
    except OSError as exc:
        raise OSError(f"Unable to create config directory: {paths.config_dir}") from exc

    if not paths.config_file.exists():
        try:
            paths.config_file.write_text(_DEFAULT_CONFIG_HEADER, encoding="utf-8")
        except OSError as exc:
            raise OSError(f"Unable to create config file: {paths.config_file}") from exc

    return paths.config_file


def load_user_config() -> dict[str, Any]:
    """Load and return user config from brain2_config.toml."""
    config_file = ensure_user_config_file()
    try:
        with config_file.open("rb") as file_handle:
            data = tomllib.load(file_handle)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigParseError(f"Invalid TOML in config file: {config_file}") from exc
    except OSError as exc:
        raise OSError(f"Unable to read config file: {config_file}") from exc

    if not isinstance(data, dict):
        raise ConfigParseError(f"Config root must be a TOML table: {config_file}")
    return data


def set_app_config(config: dict[str, Any]) -> None:
    """Store app config in module cache for app-wide access."""
    global _APP_CONFIG
    _APP_CONFIG = config


def get_app_config() -> dict[str, Any]:
    """Return cached app config; initialize first at app startup."""
    if _APP_CONFIG is None:
        raise RuntimeError("App config is not initialized. Call initialize_app_config() first.")
    return _APP_CONFIG


def initialize_app_config() -> dict[str, Any]:
    """Bootstrap and cache config for the current app process."""
    config = load_user_config()
    set_app_config(config)
    return config


def list_brains() -> list[BrainRecord]:
    """Return normalized brain records from config file."""
    config = load_user_config()
    raw_brains = config.get("brains", [])
    if not isinstance(raw_brains, list):
        raise ConfigParseError("Config key 'brains' must be an array of tables.")

    brains: list[BrainRecord] = []
    for item in raw_brains:
        if not isinstance(item, dict):
            continue
        brain_name = str(item.get("brain_name", "")).strip()
        categories_raw = item.get("categories", [])
        categories = (
            [str(entry).strip() for entry in categories_raw if str(entry).strip()]
            if isinstance(categories_raw, list)
            else []
        )
        root_folder = str(item.get("root_folder", "")).strip()
        create_named_folder = bool(item.get("create_named_folder", False))
        if brain_name:
            brains.append(
                BrainRecord(
                    brain_name=brain_name,
                    categories=categories,
                    root_folder=root_folder,
                    create_named_folder=create_named_folder,
                )
            )
    return brains


def _quote_toml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _brain_to_toml_block(brain: BrainRecord) -> str:
    categories = ", ".join(_quote_toml_string(item) for item in brain.categories)
    return (
        "[[brains]]\n"
        f"brain_name = {_quote_toml_string(brain.brain_name)}\n"
        f"categories = [{categories}]\n"
        f"root_folder = {_quote_toml_string(brain.root_folder)}\n"
        f"create_named_folder = {str(brain.create_named_folder).lower()}\n"
    )


def add_brain(
    brain_name: str,
    categories: list[str],
    root_folder: str,
    create_named_folder: bool,
) -> BrainRecord:
    """Append a new brain to TOML config and refresh in-memory cache."""
    normalized_name = brain_name.strip()
    normalized_root = root_folder.strip()
    normalized_categories = [item.strip() for item in categories if item.strip()]
    if not normalized_name:
        raise ValueError("Brain name is required.")
    if not normalized_categories:
        raise ValueError("At least one category is required.")
    if not normalized_root:
        raise ValueError("Root folder is required.")

    existing = list_brains()
    if any(item.brain_name.casefold() == normalized_name.casefold() for item in existing):
        raise ValueError(f"A brain named '{normalized_name}' already exists.")

    brain = BrainRecord(
        brain_name=normalized_name,
        categories=normalized_categories,
        root_folder=normalized_root,
        create_named_folder=create_named_folder,
    )
    config_file = ensure_user_config_file()
    try:
        prefix = "\n" if config_file.stat().st_size > 0 else ""
        with config_file.open("a", encoding="utf-8") as file_handle:
            file_handle.write(prefix + _brain_to_toml_block(brain))
    except OSError as exc:
        raise OSError(f"Unable to write config file: {config_file}") from exc

    set_app_config(load_user_config())
    return brain