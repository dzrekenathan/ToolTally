# ToolTally
# **FastAPI Project with OAuth2 Authentication and CRUD Operations**


This project is a RESTful API built using FastAPI, implementing OAuth2 authentication with JWT tokens and providing CRUD operations for user and post management.

## **Table of Contents**

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
  - [Authentication](#authentication)
  - [Endpoints](#endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## **Features**

- User registration and login system with secure password hashing.
- Token-based authentication using OAuth2 with JWT.
- CRUD operations for user and post resources.
- PostgreSQL database integration for data persistence.
- Organized and modular codebase for scalability.

---

## **Technologies**

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com)
- **Authentication**: OAuth2 with JWT
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Password Hashing**: Passlib
- **Python Libraries**: 
  - `jose` for JWT encoding/decoding
  - `pydantic` for data validation
  - `fastapi.security` for OAuth2 integration

---

## **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Set up a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your PostgreSQL database and update the `database.py` file with your connection details.

5. Run database migrations:

   ```bash
   alembic upgrade head
   ```

6. Start the server:

   ```bash
   uvicorn app.main:app --reload
   ```

---

## **Usage**

### Authentication

- Register a user using the `/users/` endpoint.
- Obtain a token by logging in at the `/token/` endpoint.

### Endpoints

#### **User Endpoints**
| Method | Endpoint     | Description                |
|--------|--------------|----------------------------|
| POST   | `/users/`    | Create a new user          |
| GET    | `/users/{id}`| Retrieve a specific user   |

#### **Post Endpoints**
| Method | Endpoint     | Description                |
|--------|--------------|----------------------------|
| GET    | `/posts/`    | Retrieve all posts         |
| POST   | `/posts/`    | Create a new post          |
| GET    | `/posts/{id}`| Retrieve a specific post   |
| DELETE | `/posts/{id}`| Delete a specific post     |
| PUT    | `/posts/{id}`| Update a specific post     |

For detailed request and response examples, refer to the API documentation at `/docs` or `/redoc`.

---

## **Project Structure**

```plaintext
├── app
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic models
│   ├── utils.py             # Utility functions
│   ├── oauth2.py            # Authentication logic
│   ├── routers
│   │   ├── __init__.py
│   │   ├── user.py          # User-related routes
│   │   ├── post.py          # Post-related routes
│   │   └── auth.py          # Authentication routes
│   └── migrations           # Alembic migrations
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## **Contributing**

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any inquiries or support, please contact:

- **Author**: [Nathan K. Dzreke-Poku]
- **Email**: dzrekenathan2002@gmail.com
- **GitHub**: [https://github.com/dzrekenathan](https://github.com/dzrekenathan)

--- 

This README provides a comprehensive guide to your project and ensures it is easy to understand and use by contributors or users.
