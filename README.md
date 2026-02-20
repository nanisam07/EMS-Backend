# 🚀 StaffPro EMS – Employment Management System (Backend)

StaffPro EMS is a production-style REST API built to power a full-stack Employment Management System.  
It supports secure role-based authentication, employee lifecycle management, and team operations with a scalable backend architecture.

🌐 **Live Frontend:** https://staffproems.vercel.app

---

## 📖 Project Overview

This backend service is designed to simulate real-world HR software where different user roles manage employees and teams through a secure and modular API.

It follows clean backend development practices and is structured for future scalability.

---

## 🧠 Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite *(update if using MySQL/PostgreSQL)*
- **API Architecture:** RESTful
- **Authentication:** Secure password hashing
- **Frontend Integration:** Next.js (Vercel deployment)

---

## ✨ Features

### 🔐 Authentication & Authorization
- Role-based login system
- Secure password hashing
- Separate dashboards for:
  - HR
  - Manager
  - CEO

### 🧑‍💼 Employee Management
- Add new employees
- View employee list
- Update employee details
- Delete employees

### 👥 Team Management
- Create teams
- Assign team leaders
- Add/remove team members

### 🔗 API Integration
- Fully connected with live frontend
- JSON-based request/response handling

---

## 🏗️ System Architecture

The backend follows a modular and scalable structure:

- Separation of routes, models, and business logic
- API-first design for frontend consumption
- Easily extendable for microservices
- Clean and readable codebase

---

## 📡 API Endpoints

### 🔹 Authentication

**POST /login**

```json
{
  "email": "hr@example.com",
  "password": "hr123"
}

| Method | Endpoint        | Description        |
| ------ | --------------- | ------------------ |
| GET    | /employees      | Get all employees  |
| POST   | /employees      | Add a new employee |
| PUT    | /employees/<id> | Update employee    |
| DELETE | /employees/<id> | Delete employee    |

| Method | Endpoint | Description       |
| ------ | -------- | ----------------- |
| GET    | /teams   | Get all teams     |
| POST   | /teams   | Create a new team |

🖥️ Frontend Integration
The backend is fully integrated with the live frontend:
🔗 https://staffproems.vercel.app
Frontend capabilities:
Role-based dashboards
Dynamic employee management
Team creation & assignment
API-powered real-time data updates

| Role    | Email                                             | Password   |
| ------- | ------------------------------------------------- | ---------- |
| HR      | [hr@example.com](mailto:hr@example.com)           | hr123      |
| Manager | [manager@example.com](mailto:manager@example.com) | manager123 |
| CEO     | [ceo@example.com](mailto:ceo@example.com)         | ceo123     |


⚙️ Local Development Setup
1️⃣ Clone the Repository
git clone https://github.com/nanisam07/<your-backend-repo-name>.git
cd <your-backend-repo-name>
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Server
python app.py

Server will start at:
👉 http://127.0.0.1:5000/

🧪 Example API Workflow
Login using /login
Receive authentication response
Perform employee & team operations
Data reflects instantly in the frontend dashboard

📂 Project Structure (Example)
staffpro-backend/
│── routes/
│── models/
│── services/
│── app.py
│── requirements.txt
🚀 Deployment

The backend is designed to be deployable on:
Render
Railway
AWS
Docker (future enhancement)

📸 Application Preview
🔐 Login Page
👥 Employee Dashboard
👥 Team Management

📈 Future Enhancements
JWT-based authentication
Role-based middleware protection
Pagination & search filters
Unit & integration testing
Docker containerization
CI/CD pipeline
Cloud database migration

🤝 Contribution
Contributions, issues, and feature requests are welcome.
If you would like to improve this project:
Fork the repository
Create a new branch
Commit your changes
Open a pull request

👨‍💻 Author
K Samuel Victor
Full-stack Developer (Next.js | Node.js | Flask)
GSoC 2026 Aspirant 🚀
