ifeq ($(OS),Windows_NT)
	ACTIVATE = . venv/Scripts/activate
else
	ACTIVATE = . venv/bin/activate
endif

build-project:
	cd frontend/ && \
	rm -rf node_modules && \
	npm install && \
	npm run build && \
	cd ../backend/ && \
	rm -rf venv && \
	python3 -m venv venv && \
	$(ACTIVATE) && \
	pip install -r requirements.txt && \
	rm -f db.sqlite3 && \
	python manage.py migrate && \
	echo "from app.models import Users; Users.objects.create_superuser(email='admin@email.com', username='admin', password='1234')" | python manage.py shell && \
	echo "from app.models import Users; Users.objects.create_user(email='user@email.com', username='user', password='1234')" | python manage.py shell

start-backend: 
	cd backend/ && \
	$(ACTIVATE) && \
	python manage.py runserver

start-frontend: 
	cd frontend/ && \
	npm start
