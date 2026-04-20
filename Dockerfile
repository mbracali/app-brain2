# Use slim debian stable image (Docker + Podman compatible)
FROM docker.io/library/python:3.14-slim-bookworm

# App labeling
LABEL app.name="app-brain2" \
      app.version="0.1.0" \
      app.created="2026-04-08" \
      app.authors="marcelo.bracali"

# Install uv on the machine to manage dependencies
RUN apt-get update && apt-get install -y curl ca-certificates \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && cp /root/.local/bin/uv /usr/local/bin/uv \
    && chmod +x /usr/local/bin/uv \
    && rm -rf /var/lib/apt/lists/*

# Create app directory before we work there
RUN mkdir -p /app

# Configure environment
ENV PATH="/usr/local/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    UV_PROJECT_ENVIRONMENT=/app/.venv

# Create non-root user and give ownership of /app
RUN useradd -m brain2_root \
    && chown -R brain2_root:brain2_root /app

USER brain2_root

# Work from /app as non-root
WORKDIR /app

# Copy project metadata first (for dependency caching)
COPY pyproject.toml uv.lock ./

# Sync uv dependencies (creates /app/.venv)
RUN uv sync --frozen --no-dev

# Copy the rest of the application to the container
COPY . .

# Web port
EXPOSE 8010

# Run the FastAPI app via uvicorn through uv
CMD ["uv", "run", "--no-sync", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8010"]

