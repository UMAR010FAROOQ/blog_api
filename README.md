# 🚀 Blog API (Django REST Framework)

A production-ready Blog API built with Django REST Framework, implementing advanced backend concepts such as authentication, permissions, nested comments, and optimized queries.

---

## 🔥 Features

* JWT Authentication (Login / Refresh Tokens)
* Owner-based permissions (secure APIs)
* Admin override system
* Blog Posts CRUD
* Category management
* Nested comment system (replies)
* Soft delete (no permanent data loss)
* Service layer architecture
* Filtering, Search, Ordering
* Pagination
* Custom API response format
* Query optimization (`select_related`, `prefetch_related`)

---

## 🧠 Tech Stack

* Python
* Django
* Django REST Framework
* SimpleJWT
* SQLite (can be replaced with PostgreSQL)

---

## 🔐 Authentication

Uses JWT Authentication:

* Login → `/jwt/login/`
* Refresh → `/jwt/refresh/`

### Header format:

Authorization: Bearer `<access_token>`

---

## 📌 API Endpoints

### 📝 Posts

* `GET /posts/`
* `POST /posts/`
* `GET /posts/{id}/`
* `PUT /posts/{id}/`
* `DELETE /posts/{id}/`

### ⚙️ Custom

* `GET /posts/my_posts/`
* `GET /posts/{id}/comments/`

### 💬 Comments

* `POST /comments/`
* Supports nested replies using `parent` field

---

## 🧪 Example Request (Create Post)

```json
{
  "title": "My Post",
  "content": "Content here",
  "is_published": true,
  "category_ids": [1]
}
```

---

## 🧠 Architecture Highlights

* Clean Service Layer separation
* Scalable permission system
* Optimized database queries
* Reusable utilities & components

---

## 🚀 Setup Instructions

```bash
git clone <your-repo-url>
cd blog_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 👨‍💻 Author

Umar Farooq
Backend Developer (Django / DRF)
