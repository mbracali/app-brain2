from contextlib import asynccontextmanager
import html
from pathlib import Path

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from src.modules.initial_setup import add_brain, get_app_config, initialize_app_config, list_brains

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
START_TEMPLATE = TEMPLATES_DIR / "brain2-start.html"


@asynccontextmanager
async def lifespan(_: FastAPI):
    initialize_app_config()
    yield


app = FastAPI(title="brain2", lifespan=lifespan)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def _render_brains_list() -> str:
    brains = list_brains()
    if not brains:
        return '<p class="sidebar-empty">No brains yet. Create your first brain.</p>'

    parts = []
    for brain in brains:
        categories = ", ".join(brain.categories)
        parts.append(
            (
                '<article class="brain-item">'
                f'<h4 class="brain-item-title">{html.escape(brain.brain_name)}</h4>'
                f'<p class="brain-item-meta">{html.escape(categories)}</p>'
                f'<p class="brain-item-path">{html.escape(brain.root_folder)}</p>'
                "</article>"
            )
        )
    return "".join(parts)


def _render_modal(error_message: str = "") -> str:
    error_html = (
        f'<p class="modal-error" role="alert">{html.escape(error_message)}</p>'
        if error_message
        else ""
    )
    return (
        '<div class="overlay-backdrop" id="brain-modal-backdrop">'
        '<div class="brain-modal" role="dialog" aria-modal="true" aria-label="Create brain">'
        '<form id="brain-create-form" '
        'hx-post="/brains/create" hx-target="#brains-list" hx-swap="outerHTML">'
        '<header class="modal-section">'
        '<input class="modal-input" type="text" name="brain_name" '
        'placeholder="my-awesome-brain2" required />'
        '<p class="modal-help">Name this brain</p>'
        "</header>"
        '<hr class="modal-separator" />'
        '<section class="modal-section modal-categories">'
        '<label><input type="checkbox" name="categories" value="Scholar &amp; Study" /> '
        "Scholar &amp; Study</label>"
        '<label><input type="checkbox" name="categories" value="Work" /> Work</label>'
        '<label><input type="checkbox" name="categories" value="Personal Projects" /> '
        "Personal Projects</label>"
        "</section>"
        '<hr class="modal-separator" />'
        '<section class="modal-section">'
        '<p class="modal-help">Select a folder to store data (Select the root folder)</p>'
        '<input id="folder-path" class="modal-input" type="text" name="root_folder" '
        'placeholder="/path/to/root/folder" required />'
        '<div class="folder-row">'
        '<button class="new-brrain-btn modal-select-btn" type="button" id="folder-picker-btn">'
        "Select a folder"
        "</button>"
        '<label class="inline-toggle">'
        '<input type="checkbox" name="create_named_folder" value="true" />'
        "<span>Create a folder with brain name</span>"
        "</label>"
        "</div>"
        '<input id="folder-picker-input" type="file" webkitdirectory directory multiple hidden />'
        "</section>"
        f"{error_html}"
        '<footer class="modal-footer">'
        '<button id="create-brain-btn" class="new-brrain-btn" type="submit" disabled>Create</button>'
        '<button class="modal-close-btn" hx-get="/brains/modal/close" hx-target="#modal-root" '
        'hx-swap="innerHTML" type="button">Cancel</button>'
        "</footer>"
        "</form>"
        "</div>"
        '<script>window.brain2SetupModal && window.brain2SetupModal();</script>'
        "</div>"
    )


@app.get("/")
async def start_screen() -> HTMLResponse:
    template = START_TEMPLATE.read_text(encoding="utf-8")
    page = template.replace("<!-- BRAINS_LIST_PLACEHOLDER -->", _render_brains_list())
    return HTMLResponse(page)


@app.get("/brains/list")
async def brains_list() -> HTMLResponse:
    return HTMLResponse(f'<div id="brains-list" class="brains-list">{_render_brains_list()}</div>')


@app.get("/brains/modal")
async def brains_modal() -> HTMLResponse:
    return HTMLResponse(_render_modal())


@app.get("/brains/modal/close")
async def brains_modal_close() -> HTMLResponse:
    return HTMLResponse("")


@app.post("/brains/create")
async def create_brain(
    brain_name: str = Form(...),
    categories: list[str] | None = Form(default=None),
    root_folder: str = Form(...),
    create_named_folder: str | None = Form(default=None),
) -> HTMLResponse:
    try:
        add_brain(
            brain_name=brain_name,
            categories=categories or [],
            root_folder=root_folder,
            create_named_folder=create_named_folder is not None,
        )
    except ValueError as exc:
        return HTMLResponse(
            f'<div id="brains-list" class="brains-list">{_render_brains_list()}</div>'
            f'<div id="modal-root" hx-swap-oob="innerHTML">{_render_modal(str(exc))}</div>',
            status_code=400,
        )

    return HTMLResponse(
        f'<div id="brains-list" class="brains-list">{_render_brains_list()}</div>'
        '<div id="modal-root" hx-swap-oob="innerHTML"></div>'
    )


@app.get("/health")
async def health() -> JSONResponse:
    config = get_app_config()
    return JSONResponse({"status": "ok", "config_keys": sorted(config.keys())})
