# FundStarter API 🚀

FundStarter is a professional and robust backend API for a crowdfunding platform. Built with **Python** and **Django Rest Framework (DRF)**, it provides a secure environment for creators to raise funds and for backers to support innovative projects.

---

## 🌟 Key Features

### 🔐 1. Advanced Authentication
- **Custom User Model:** Modern authentication using **Email** as the primary identifier instead of a username.
- **JWT Security:** Secure, stateless login system using JSON Web Tokens (`SimpleJWT`).

### 📢 2. Campaign Management
- **Full CRUD:** Comprehensive system to create, view, and manage crowdfunding campaigns.
- **Visual Content:** Support for **Campaign Images** to make projects more attractive.
- **Progress Tracking:** Real-time calculation of **Funding Percentage** (Progress Bar data) via API.
- **Owner Security:** Advanced permissions; only the creator can edit or delete their campaign.

### 💸 3. Smart Donation System
- **Transaction Integrity:** Secure donation flow with strict business logic.
- **Automated Aggregation:** Used **Django Signals** to automatically update the campaign's total funds whenever a donation is made.
- **Robust Validation:**
  - Prevents creators from donating to their own projects.
  - Ensures donations are positive amounts.
  - Blocks donations to campaigns that have passed their **Deadline**.

### 🔍 4. Professional API Features
- **Interactive Documentation:** Full **Swagger UI** and **Redoc** integration using `drf-spectacular`.
- **Search & Discovery:** Powerful keyword search and multiple ordering options (by target, date, or deadline).
- **Improved Readability:** Nested data representation in API responses for better developer experience (Human-readable campaign titles in lists).

---

## 🛠 Tech Stack
- **Framework:** Django & Django Rest Framework (DRF)
- **Authentication:** SimpleJWT
- **Documentation:** drf-spectacular (Swagger/OpenAPI 3.0)
- **Image Processing:** Pillow
- **Database:** SQLite (Development) / Ready for PostgreSQL

---

## 🔌 API Endpoints (Quick Overview)

| Method   | Endpoint              | Description                                      |
|:---------|:----------------------|:-------------------------------------------------|
| **POST** | `/api/token/`         | Login & Receive JWT Tokens                       |
| **GET**  | `/api/docs/`          | **Interactive Swagger Documentation**            |
| **GET**  | `/api/campaigns/`     | List all campaigns (with Search/Order)           |
| **POST** | `/api/campaigns/`     | Create a new project (Authenticated)             |
| **POST** | `/api/donation/`      | Support a project with a donation                |

---
