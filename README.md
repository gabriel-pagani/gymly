# Description

# Installation and Configuration (Linux/Mac)
### Start
```bash
git clone https://github.com/gabriel-pagani/none.git && cd none/
```

### Backend (Django)
```bash
cd backend/
```
```bash
python3 -m venv venv && source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```

### Frontend (React)
```bash
cd ../frontend/
```
```bash
npm install
```
```bash
npm run build
```

# Project Structure
```
none/
├── backend/
│   ├── app/
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

