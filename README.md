
# 🧠 Django Quiz App

A full-stack Django application featuring custom user authentication, profile management, and a REST API-based quiz module. Ideal for educational platforms and skill-assessment tools.

---

## 📁 Folder Structure

<img width="836" height="1197" alt="Project Structure" src="https://github.com/user-attachments/assets/5ac5a05a-8dbe-45f2-922b-93f029e490b6" />

---

## 🚀 Features

- 🔐 Custom user authentication (signup, login, logout)
- ✅ Email activation for new accounts
- 👤 User profile and personalized dashboard
- 📊 Quiz module via REST API
- 🖼️ Profile image upload support
- 🛠️ Django Admin Panel for backend control
- 🌐 Template-based frontend (HTML/CSS)

---

## 🛠️ Technologies Used

- **Backend**: Django 4.x
- **API**: Django REST Framework
- **Database**: SQLite
- **Frontend**: HTML5, CSS3
- **Authentication**: Token + Email verification
- **Media Handling**: Django file upload system

---

## 🔧 Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/django-quiz-app.git
cd django-quiz-app/backend

# 2. Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create Admin User
python manage.py createsuperuser

# 6. Run Development Server
python manage.py runserver
```

---

## 📬 Quiz API Endpoints

| Method | Endpoint                 | Description              |
|--------|--------------------------|--------------------------|
| GET    | `/quiz/`                 | List all quizzes         |
| GET    | `/quiz/<id>/`            | Get quiz by ID           |
| POST   | `/quiz/<id>/submit/`     | Submit answers to quiz   |

Built with Django REST Framework and returns JSON responses.

---

## 👤 User Authentication Flow

1. **Signup**: Register with name, email, and password  
2. **Email Activation**: Activate via link sent to inbox  
3. **Login**: Access account post-activation  
4. **Dashboard/Profile**: View progress and manage details  
5. **Logout**: Securely end session  

---

## 📸 Screenshots

<div align="center">
  <img src="https://github.com/user-attachments/assets/160898b8-8d7d-417d-916c-143277056fc5" alt="Landing Page" style="max-width: 90%; border-radius: 12px;" />
  <p><b>🔹 AI-Powered Landing Page</b></p>
  <br><br>

  <img src="https://github.com/user-attachments/assets/ec0bd1df-baa5-4f8e-935d-98d53a95c5a7" alt="Dashboard View" style="max-width: 90%; border-radius: 12px;" />
  <p><b>📊 Personalized Dashboard with Learning Path</b></p>
  <br><br>

  <img src="https://github.com/user-attachments/assets/6d4630f6-b8aa-45b9-ac34-a5795520db4a" alt="Performance Chart" style="max-width: 90%; border-radius: 12px;" />
  <p><b>📈 Performance Score Visualization</b></p>
  <br><br>

  <img src="https://github.com/user-attachments/assets/897d020a-d33d-4f62-8e55-7dbd99b7ca06" alt="Adaptive Quiz" style="max-width: 90%; border-radius: 12px;" />
  <p><b>🧠 Adaptive Quiz Suggestions</b></p>
  <br><br>

  <img src="https://github.com/user-attachments/assets/71b44885-239c-4b68-a2f5-16cff34baa7b" alt="Progress Reports" style="max-width: 90%; border-radius: 12px;" />
  <p><b>📘 AI-Generated Progress Reports</b></p>
</div>

---

## 📂 Static & Media Files

- **Media**: Uploaded profile images → `media/profiles/`  
- **Static**: CSS, JS, and image assets → `static/`  

### Django settings required:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

### In `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 👨‍💻 Contribution Guidelines

1. Fork the repository  
2. Create a new branch: `git checkout -b feature/my-feature`  
3. Commit your changes: `git commit -m 'Add new feature'`  
4. Push to the branch: `git push origin feature/my-feature`  
5. Open a pull request 🚀

---
