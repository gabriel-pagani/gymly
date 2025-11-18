build-project:
	touch .env backend/project/local_settings.py && \
	cd frontend/ && npm install && npm run build && \
	docker compose up -d --build

clean-project:
	docker compose down && \
	docker system prune -a --volumes --force && \
    rm -rf database frontend/node_modules/ backend/build/

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

backend-terminal:
	docker compose exec backend $(filter-out $@,$(MAKECMDGOALS))
%:
	@:
