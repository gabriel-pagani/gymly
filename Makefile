ifeq ($(OS),Windows_NT)
	FOLDER = Scripts
else
	FOLDER = bin
endif

build-project:
	cd frontend/ && \
	rm -rf node_modules && \
	npm install && \
	npm run build && \
	cd ../backend/ && \
	touch project/local_settings.py && \
	rm -rf venv && \
	python3 -m venv venv && \
	. venv/$(FOLDER)/activate && \
	python -m pip install --upgrade pip && \
	pip install -r requirements.txt && \
	rm -f db.sqlite3 && \
	python manage.py migrate && \
	echo "from app.models import Users; Users.objects.create_superuser(email='admin@email.com', username='admin', password='1234')" | python manage.py shell && \
	echo "from app.models import Users; Users.objects.create_user(email='user@email.com', username='user', password='1234')" | python manage.py shell

start-backend: 
	cd backend/ && \
	. venv/$(FOLDER)/activate && \
	python manage.py runserver

start-frontend: 
	cd frontend/ && \
	npm start
