# FundStarter API 🚀

FundStarter is a backend API for a crowdfunding platform. It is built with **Python**, **Django**, and **Django Rest Framework (DRF)**. In this platform, users can create campaigns to raise money for their projects, and other users can support them by donating money.

## 🌟 Key Features

### 1. User Authentication
*   **Custom User Model:** Users log in with **Email** instead of a username.
*   **JWT Security:** Uses JSON Web Tokens (SimpleJWT) for secure login and access.

### 2. Campaign Management
*   **Full CRUD:** Users can create, view, update, and delete campaigns.
*   **Owner Security:** Only the person who created the campaign can edit or delete it. Others can only view it.
*   **Deadline:** Each campaign has a date when it ends.

### 3. Donation System
*   **Support Projects:** Users can send money to active campaigns.
*   **Business Logic:**
    *   You cannot donate to your own campaign.
    *   You cannot donate 0 or negative amounts.
    *   You cannot donate to a campaign if the deadline has passed.

### 4. Smart Backend (Signals)
*   **Auto-Update:** I used **Django Signals** to automatically update the `current_amount` of a campaign every time a new donation is successfully saved.

### 5. Advanced Search
*   **Search:** Find campaigns by searching for keywords in the title or description.
*   **Ordering:** Sort campaigns by creation date, target money, or deadline.

---

## 🛠 Tech Stack
*   **Framework:** Django & Django Rest Framework (DRF)
*   **Auth:** SimpleJWT
*   **Database:** SQLite (Development)
