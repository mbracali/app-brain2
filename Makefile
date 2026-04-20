# Set the shell to /bin/sh for all Makefile recipe commands
SHELL := /bin/sh

# Detect compose command with clear fallback order:
# (1) podman compose, (2) podman-compose, (3) docker compose
COMPOSE := $(shell \
	if command -v podman >/dev/null 2>&1; then \
		echo "podman compose"; \
	elif command -v podman-compose >/dev/null 2>&1; then \
		echo "podman-compose"; \
	elif command -v docker >/dev/null 2>&1; then \
		echo "docker compose"; \
	fi \
)

# Set the default Makefile goal to the 'help' target
.DEFAULT_GOAL := help

# Declare make targets as 'phony', these are the commands the user can run
.PHONY: check-compose help build rebuild up up-d run down logs ps restart clean

# check-compose: Ensures a compatible compose tool is available; errors out if not
check-compose:
	@if [ -z "$(COMPOSE)" ]; then \
		echo "Error: no compatible compose tool found."; \
		echo "Install Docker (docker compose) or Podman (podman compose / podman-compose)."; \
		exit 1; \
	fi

# help: Shows available targets and usage
help: check-compose
	@echo ""
	@echo "Using: $(COMPOSE)"
	@echo ""
	@echo "Targets:"
	@echo "  build     Build images using cache"
	@echo "  rebuild   Build images without cache"
	@echo "  up        Start stack in foreground"
	@echo "  up-d      Start stack in detached mode"
	@echo "  run       Alias to up"
	@echo "  down      Stop and remove stack resources"
	@echo "  logs      Follow service logs"
	@echo "  ps        Show service status"
	@echo "  restart   Restart stack (detached)"
	@echo "  clean     Down + remove orphans, images and volumes"
	@echo ""

# build: Build images using cache
build: check-compose
	$(COMPOSE) build

# rebuild: Build images without cache
rebuild: check-compose
	$(COMPOSE) build --no-cache

# up: Start stack in foreground
up: check-compose
	$(COMPOSE) up

# up-d: Start stack in detached mode
up-d: check-compose
	$(COMPOSE) up -d

# run: Alias to up
run: up

# down: Stop and remove stack resources
down: check-compose
	$(COMPOSE) down --remove-orphans

# logs: Follow service logs
logs: check-compose
	$(COMPOSE) logs -f

# ps: Show service status
ps: check-compose
	$(COMPOSE) ps

# restart: Restart stack (detached, force rebuild)
restart: check-compose
	$(COMPOSE) down --remove-orphans
	$(COMPOSE) up -d --build

# clean: Remove orphans, images and volumes (clean stack)
clean: check-compose
	$(COMPOSE) down --remove-orphans --rmi local --volumes

