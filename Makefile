build-system:
	touch .env backend/project/local_settings.py && \
	cd frontend/ && npm install && npm run build && \
	docker compose pull db && \
	docker compose build

delete-system:
	docker compose down && \
    docker system prune -a --volumes --force && \
    rm -rf database

start-system:
	docker compose up -d
	@echo ""
	@echo "Starting the system in http://127.0.0.1:8000/"

stop-system:
	docker compose down

restart-system:
	docker compose down && \
	docker compose up -d
	@echo ""
	@echo "Restarting the system in http://127.0.0.1:8000/"

create-superuser:
	docker exec -it app python manage.py createsuperuser
