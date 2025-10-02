# Description

# Installation and Configuration (Linux/Mac)
### Start
```
git clone https://github.com/gabriel-pagani/none.git && cd none/
```

### Backend (Django)
```
cd backend/
```
```
python3 -m venv venv && source venv/bin/activate
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

### Frontend (React)
```
cd ../frontend/
```
```
npm install
```
```
npm run build
```

# Project Structure
```
none/
├── backend/
│   ├── app/
│   ├── build/
│   ├── project/
│   ├── venv/
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   ├── .gitignore
│   ├── package-lock.json
│   ├── package.json
│   └── README.md
├── .gitignore
├── LICENSE
└── README.md
```

# How to Use

# License
See the [LICENSE](https://github.com/gabriel-pagani/none/blob/main/LICENSE) file for more details.

# Contact Information
Email: gabrielpaganidesouza@gmail.com

