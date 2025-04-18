# Late Show API

A Flask-based RESTful API for tracking guests and their appearances in talk show episodes.

---

## 📦 Project Overview

This API allows clients to:

- List all episodes
- View a single episode with its guest appearances
- Delete an episode
- List all guests
- Create an appearance with validation

It uses Flask, SQLAlchemy for ORM, and Flask-Migrate for database migrations.

---

## 🛠 Tech Stack

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite (for development)
- Postman (for API testing)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/WambuiJoan-dev/lateshow-Wambui-Joan.git
cd lateshow-Wambui-Joan
```

### 2. Create & Activate a Virtual Environment

```bash
pipenv install
pipenv shell
```

### 3. Install Dependencies

```bash
pip install 
```

### 4. Set Up the Database

```bash
export FLASK_APP=app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Seed the Database

```bash
python seed.py
```

### 6. Start the Server

```bash
flask run
```

Visit `http://localhost:5555` to access the API.

---

## 📮 API Endpoints

| Method | Endpoint             | Description                          |
|--------|----------------------|--------------------------------------|
| GET    | /episodes            | List all episodes                    |
| GET    | /episodes/<id>       | Get a specific episode with guests   |
| DELETE | /episodes/<id>       | Delete a specific episode            |
| GET    | /guests              | List all guests                      |
| POST   | /appearances         | Create an appearance (with rating)   |

**POST /appearances Example Request**
```json
{
  "rating": 5,
  "episode_id": 2,
  "guest_id": 3
}
```

---

## 🧪 Testing with Postman

1. Open Postman.
2. Import the collection file: `challenge-4-lateshow.postman_collection.json`.
3. Send requests to `http://localhost:5555`.

---

## ✅ Validations

- Appearance `rating` must be between `1` and `5`.
- `episode_id` and `guest_id` must refer to valid records.

---

## 📁 Project Structure

```
.
├── app.py
├── config.py
├── models.py
├── routes.py
├── seed.py
├── migrations/
├── README.md
├── requirements.txt
└── challenge-4-lateshow.postman_collection.json
```

---

## 👩‍💻 Author

- Wambui [GitHub](https://github.com/WambuiJoan-dev)

---

## 📜 License
