# 🩸 Blood Donation Platform

A smart donation platform built with **Django** where users can create posts for blood needs, search donors, request donations, and manage their donation history. It connects people in need with available donors efficiently.

---

## 🚀 Features

- ✅ **User Authentication** (Register/Login)
- 📢 **Post Creation** for blood requests
- 👥 **Donor List** with last donation date
- 🔁 **Request Donors** who are eligible (after 21 days)
- 💬 **Comment on Posts**
- ❌ **Delete Own Posts**
- 🔎 **Search by Username or Blood Group**
- 🖼️ Profile and media upload support

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Database:** SQLite3 (default for development)
- **Frontend:** HTML, CSS, Bootstrap
- **Other:** Django ORM, Authentication, Admin Panel

---

## 📁 Project Structure
BDG/ ├── Blood-Donation/ # Django project root ├── accounts/ # User authentication and management ├── media/ # Uploaded media files ├── newsfeed/ # Post creation, comment system ├── profiles/ # User profile and donor data ├── static/ # Static files (CSS, JS, images) ├── templates/ # HTML templates ├── db.sqlite3 # SQLite database └── manage.py # Django management script

