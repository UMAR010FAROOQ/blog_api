# 🚀 DRF Blog API

A production-oriented Blog API built with Django REST Framework, implementing authentication, clean architecture, API versioning, and automated testing.

---

## 🔥 Features

* ✅ API Versioning (`/api/v1/`)
* 🔐 JWT Authentication (Login + Refresh)
* 🧱 Structured Auth Routes (`/api/auth/`)
* 🛡️ Permission-based Access Control
* 📝 Blog Posts CRUD
* 💬 Nested Comment System (replies supported)
* ♻️ Soft Delete (no permanent data loss)
* 🧠 Service Layer Architecture
* 🔍 Filtering, Search, Ordering
* 📄 Pagination
* 📦 Custom API Response Format
* ⚡ Query Optimization (`select_related`, `prefetch_related`)
* 🧪 Automated API Testing (`APITestCase`)
* 🚀 CI Pipeline (GitHub Actions)
* 📘 API Documentation (Swagger via drf-spectacular)

---

## 🧠 Tech Stack

* Python
* Django
* Django REST Framework
* SimpleJWT
* drf-spectacular (Swagger)
* SQLite (can be replaced with PostgreSQL)

---

## 🔐 Authentication

JWT-based authentication:

* Login → `/api/auth/login/`
* Refresh → `/api/auth/refresh/`

### Header format:

Authorization: Bearer `<access_token>`

---

## 📌 API Structure

### Versioned Base URL:

```id="v1base"
/api/v1/
```

---

### 📝 Posts

* `GET /posts/`
* `POST /posts/`
* `GET /posts/{id}/`
* `PUT /posts/{id}/`
* `DELETE /posts/{id}/`

---

### 💬 Comments

* `POST /comments/`
* Nested replies supported using `parent` field

---

### ⚙️ Custom Endpoints

* `GET /posts/my_posts/`
* `GET /posts/{id}/comments/`

---

## 📘 API Documentation

Swagger UI available at:

```id="swagger"
/api/docs/
```

---

## 🧪 Testing

Run tests:

```bash id="testcmd"
python manage.py test
```

Includes:

* API endpoint testing
* Authentication testing
* Permission validation

---

## 🔄 CI/CD (GitHub Actions)

Automated pipeline runs on every push:

* Install dependencies
* Run tests
* Validate code integrity

---

## 🧠 Architecture Decisions

### 🔹 Service Layer

Business logic is separated from views to:

* Improve maintainability
* Enable reusability
* Simplify testing

### 🔹 Custom Response Format

Ensures consistent API responses across all endpoints.

### 🔹 Soft Delete

Prevents permanent data loss and allows recovery.

### 🔹 API Versioning

Ensures backward compatibility and future scalability.

### 🔹 Query Optimization

Used `select_related` and `prefetch_related` to reduce DB queries.

---

## 🧪 Example Request (Create Post)

```json id="reqexample"
{
  "title": "My Post",
  "content": "Content here",
  "is_published": true,
  "category_ids": [1]
}
```

---

## 🚀 Setup Instructions

```bash id="setupcmd"
git clone https://github.com/UMAR010FAROOQ/drf-blog-api.git
cd drf-blog-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 👨‍💻 Author

Umar Farooq
Backend Developer (Django / DRF)
