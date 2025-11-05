# Installation and Configuration (Linux/Mac)
### Start
```
git clone https://github.com/gabriel-pagani/dashboards-center.git
```
```
cd dashboards-center/
```

### Frontend (React)
```
cd frontend/
```
```
npm install
```
```
npm run build
```

### Backend (Django)
```
cd ../backend/
```
```
touch project/local_settings.py
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```

# License
See the [LICENSE](https://github.com/gabriel-pagani/dashboards-center/blob/main/LICENSE) file for more details.

# Contact Information
Email: gabrielpaganidesouza@gmail.com
