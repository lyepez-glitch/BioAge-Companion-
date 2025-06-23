# 🧬 BioAgeCompanion Backend (Django + PostgreSQL)

This is the backend API for **BioAgeCompanion**, a wellness mobile app that estimates biological age and provides custom health recommendations.

Built with **Django**, **GraphQL (Graphene)**, and **PostgreSQL**. This API handles authentication, user data, biological age calculation logic, and health recommendation delivery.

---

## ⚙️ Features

- 🔐 JWT-based user authentication (GraphQL + REST support)
- 📦 REST and GraphQL APIs with Django REST Framework and Graphene
- 📊 Stores user health metrics (age, height, weight, heart rate, etc.)
- 🧠 Computes estimated biological age
- 🧾 Returns personalized health improvement suggestions
- 🌐 CORS enabled for frontend integration (e.g., Vercel/Expo)

---

## 🛠️ Tech Stack

- **Django 4.2.8**
- **PostgreSQL**
- **Graphene / GraphQL**
- **Django REST Framework**
- **Simple JWT + django-graphql-jwt**
- **CORS Headers**
- **Deployed on Render (or locally with `.env`)**

---

## 📁 Project Structure

myproject/
│
├── core/ # Custom app with models, schema, API logic
├── myproject/ # Django project settings and config
├── manage.py
└── requirements.txt


---

## 🔐 Environment Variables (`.env`)

Create a `.env` file in the root directory with the following:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=5432
🚀 Getting Started
1. Clone the Repository

git clone <your-bitbucket-repo-url>
cd backend

2. Create & Activate a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Requirements

pip install -r requirements.txt

4. Apply Migrations

python manage.py migrate

5. Run the Server

python manage.py runserver

Server runs at http://127.0.0.1:8000/

🔧 GraphQL Endpoint
GraphQL endpoint (via Graphene):

arduino

http://127.0.0.1:8000/graphql/

Supports JWT-based queries and mutations.

✅ CORS Configuration

CORS is enabled for:

http://localhost:8081

https://bio-age-frontend.vercel.app

Modify ALLOWED_HOSTS and CORS_ALLOWED_ORIGINS in settings.py as needed.

🧪 Running Tests

pytest

Ensure you’ve installed pytest and test dependencies from requirements.txt.

📄 License
This project is licensed under the 0BSD license.

✍️ Author
Lucas Yepez
Creator of BioAgeCompanion — a personal health insight tool.
