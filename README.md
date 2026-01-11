# MyJournal - Personal Daily Diary Web Application

A beautiful, secure, and feature-rich journaling web application built with Flask, SQLAlchemy, and Tailwind CSS.

![MyJournal](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

- **User Authentication** - Secure signup/login with password hashing
- **Create Entries** - Write journal entries with titles and content
- **Edit & Delete** - Full CRUD operations on your entries
- **Search Functionality** - Search through all your entries
- **Responsive Design** - Beautiful UI that works on all devices
- **Real-time Word Counter** - Track your writing progress
- **Auto-save Drafts** - Never lose your thoughts
- **Dashboard Analytics** - View your journaling statistics

## 🚀 Live Demo

🔗 **[View Live Application](https://your-app-name.onrender.com)**

## 📸 Screenshots

### Homepage
Beautiful landing page with login/signup functionality

### Dashboard
View all your journal entries in a beautiful grid layout

### Create Entry
Write your thoughts with live word counter and auto-save

## 🛠️ Tech Stack

- **Backend:** Python Flask 3.0.0
- **Database:** SQLite (SQLAlchemy ORM)
- **Frontend:** HTML5, Tailwind CSS, JavaScript
- **Authentication:** Werkzeug (Password Hashing)
- **Deployment:** Render (Gunicorn WSGI Server)

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

## 🔧 Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/aman-Tomar-30/myjournal.git
cd myjournal
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open in browser**
```
http://localhost:5000
```

## 📁 Project Structure

```
myjournal/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── render.yaml            # Render deployment config
├── .gitignore             # Git ignore file
│
├── templates/
│   ├── index.html         # Homepage
│   ├── dashboard.html     # User dashboard
│   ├── create_entry.html  # Create new entry
│   ├── view_entry.html    # View single entry
│   ├── edit_entry.html    # Edit entry
│   ├── search_results.html # Search results
│   ├── contact.html       # Contact page
│   └── about.html         # About page
│
└── instance/
    └── myjournal.db       # SQLite database (auto-created)
```

## 🚀 Deployment to Render

### Step 1: Prepare Your Repository

Ensure all files are committed:
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy on Render

1. Go to [render.com](https://render.com) and sign up
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name:** myjournal
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **"Create Web Service"**
6. Wait 2-3 minutes for deployment ✅

Your app will be live at: `https://your-app-name.onrender.com`

### Step 3: Set Environment Variables (Optional)

In Render dashboard, add:
- `SECRET_KEY`: Your secret key (auto-generated)
- `PYTHON_VERSION`: 3.11.0

## 🔐 Security Features

- ✅ Password hashing with pbkdf2:sha256
- ✅ User ownership validation
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ Session-based authentication
- ✅ CSRF protection
- ✅ Environment variable configuration

## 📊 Database Schema

### User Table
- `id` - Primary Key
- `name` - User's full name
- `email` - Unique email address
- `password` - Hashed password
- `created_at` - Account creation timestamp

### JournalEntry Table
- `id` - Primary Key
- `title` - Entry title
- `content` - Entry content
- `created_at` - Entry creation timestamp
- `user_id` - Foreign Key (User)

## 🎯 Usage

1. **Sign Up** - Create a new account
2. **Login** - Access your dashboard
3. **Write** - Create journal entries
4. **Search** - Find specific entries
5. **Edit** - Modify existing entries
6. **Delete** - Remove unwanted entries

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Aman Tomar**

- 📧 Email: amantomar2609@gmail.com
- 💼 LinkedIn: [linkedin.com/in/tomaraman](https://linkedin.com/in/tomaraman)
- 🐙 GitHub: [github.com/aman-Tomar-30](https://github.com/aman-Tomar-30)

## 🙏 Acknowledgments

- Built as part of college project at JECRC University
- Inspired by Smart India Hackathon 2023 experience
- Thanks to Flask and Tailwind CSS communities

## 📈 Future Enhancements

- [ ] Export entries to PDF
- [ ] Categories and tags
- [ ] Rich text editor
- [ ] Dark mode
- [ ] Email notifications
- [ ] Data analytics dashboard
- [ ] Mobile app (React Native)

---

⭐ **Star this repo if you found it helpful!**

Made with ❤️ by Aman Tomar