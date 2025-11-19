build-project:
	touch .env backend/project/local_settings.py && \
	cd frontend/ && npm install && npm run build && \
	docker compose up -d --build

clean-project:
	docker compose down && \
	docker system prune -a --volumes --force && \
    rm -rf backend/build/ backend/static/ database/ frontend/node_modules/

start-system:
	docker compose up -d

stop-system:
	docker compose down

restart-system:
	docker compose down && \
	docker compose up -d

container ?= backend
container-terminal:
	docker compose exec $(container) sh
