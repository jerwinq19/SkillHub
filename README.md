# 💻 Django Full-Stack Web App  

A simple yet powerful **full-stack web application** built using **Django**, designed to demonstrate clean architecture, modular development, and efficient backend logic.  

---

## 🚀 Features  

✅ User authentication (login, register, logout)  
✅ CRUD operations (Create, Read, Update, Delete)  
✅ Dynamic templates with Bootstrap  
✅ Django ORM for database management  
✅ Organized app structure for scalability  

---

## 🛠️ Tech Stack  

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Backend** | Django 5 (Python) |
| **Database** | SQLite (default) |
| **Environment** | Virtualenv |
| **Version Control** | Git & GitHub |

---

## ⚙️ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone [https://github.com/jerwinq19/SkillHub.git]
cd SkillHub
```

### 2️⃣ Create a Virtual Environment  
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment  
**Windows:**
```bash
venv\Scripts\activate
```
**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 5️⃣ Run Database Migrations  
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the Development Server  
```bash
python manage.py runserver
```

Then open your browser and visit:  
👉 **http://127.0.0.1:8000/**  

---

## 🧩 Project Structure  

```
📁 your_project/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── 📁 app_name/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── forms.py
│
└── 📁 your_project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 🧠 Developer Notes  

- Use a `.env` file to store sensitive keys (SECRET_KEY, DB credentials, etc.)  
- Always run `python manage.py collectstatic` before deployment  
- Consider deploying to **Render**, **Railway**, or **Vercel (via Django adapter)** for free hosting  

---

## 👨‍💻 Author  

**Jerwin Quijano**  
📅 *2025*  
📧 *[Add your contact or GitHub link here]*  

---
