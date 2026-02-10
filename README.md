# Django Blog 📝

A simple yet functional **blog application built with Django**, developed as part of my backend learning journey.

This project focuses on understanding Django’s core concepts such as models, views, templates, authentication, and database interactions.

---

## 🎯 Project Goals

- Learn Django framework fundamentals
- Build a real-world CRUD-based web application
- Understand Django MTV architecture
- Practice clean backend structure
- Prepare for larger, production-ready Django projects

---

## ✨ Features

- User authentication (login / logout)
- Create, edit, and delete blog posts
- Post detail and list views
- Admin panel for managing content
- Database integration using Django ORM

_(More features will be added over time.)_

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (Django Templates)
- **Database:** SQLite (default)
- **Authentication:** Django Auth System

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/AmineTabrizi/Django-Learning-Advanced.git
cd django-blog
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
