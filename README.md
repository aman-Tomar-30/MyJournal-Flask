# 📔 MyJournal - Personal Daily Diary Web Application

<div align="center">

![MyJournal Banner](https://img.shields.io/badge/MyJournal-Daily%20Diary-purple?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQgNEg4VjIwSDRWNFoiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGQ9Ik0xMCA0SDE4VjIwSDEwVjRaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4=)

**A beautiful, secure, and feature-rich journaling platform built with Flask**

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=flat-square)](https://myjournal-9h9n.onrender.com)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=flat-square&logo=github)](https://github.com/aman-Tomar-30/MyJournal-Flask)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-black?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

[Live Demo](https://myjournal-9h9n.onrender.com) • [Report Bug](https://github.com/aman-Tomar-30/MyJournal-Flask/issues) • [Request Feature](https://github.com/aman-Tomar-30/MyJournal-Flask/issues)

</div>

---

## 📖 Table of Contents

- [About The Project](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-about-the-project)
- [Features](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-features)
- [Tech Stack](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#%EF%B8%8F-tech-stack)
- [Getting Started](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Locally](#running-locally)
- [Deployment](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-deployment)
- [Usage](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-usage)
- [Admin Panel](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#%EF%B8%8F-admin-panel)
- [Project Structure](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-project-structure)
- [API Routes](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-api-routes)
- [Environment Variables](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-environment-variables)
- [Contributing](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-contributing)
- [License](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-license)
- [Contact](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#%E2%80%8D-contact)
- [Notes](https://github.com/aman-Tomar-30/MyJournal-Flask?tab=readme-ov-file#-notes)

---

## 🌟 About The Project 

**MyJournal** is a full-stack personal diary web application that provides users with a private, secure space to document their thoughts, experiences, and memories. Built with modern web technologies, it features a beautiful user interface, comprehensive admin dashboard, and robust security measures.

### ✨ Why MyJournal?

- 🔒 **Private & Secure** - Your thoughts are encrypted and protected
- 🎨 **Beautiful Design** - Modern, responsive UI with smooth animations
- 📊 **Admin Dashboard** - Complete monitoring and analytics system
- 📱 **Mobile Friendly** - Write from anywhere, on any device
- ⚡ **Fast & Reliable** - Built with performance in mind

---

## 🚀 Features

### User Features

- ✅ **User Authentication**
  - Secure signup and login
  - Password hashing with Werkzeug
  - Session-based authentication
  - "Remember me" functionality

- ✅ **Journal Entry Management**
  - Create rich journal entries
  - Edit existing entries
  - Delete entries with confirmation
  - View entry history
  - Real-time word counter
  - Auto-save drafts (localStorage)

- ✅ **Dashboard**
  - Personal statistics
  - Entry count tracking
  - Writing streak display
  - Recent entries feed

### Admin Features

- 🛡️ **Admin Dashboard**
  - Real-time statistics
  - User management
  - Content moderation
  - Activity monitoring

- 📊 **Analytics**
  - Total users and entries
  - Daily active users
  - Most active users leaderboard
  - Entry trends

- 👥 **User Management**
  - View all registered users
  - User profile details
  - Entry count per user
  - Activity tracking

- 📝 **Content Management**
  - View all entries
  - Entry statistics
  - Word count analysis
  - Full entry preview

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Flask 3.0.0
- **Database:**  Supabase's PostgreSQL / SQLite 
- **ORM:** SQLAlchemy 3.1.1
- **Security:** Werkzeug 3.0.1 (Password Hashing)
- **Server:** Gunicorn 21.2.0

### Frontend
- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first styling
- **JavaScript (Vanilla)** - Interactive features
- **FontAwesome** - Icons

### Deployment
- **Platform:** Render
- **Database:** Managed Supabase / SQLite
- **Environment:** Production-ready with environment variables

### Development Tools
- **Version Control:** Git, GitHub
- **Code Editor:** VS Code
- **Package Manager:** pip
- **Virtual Environment:** .venv

---

## 🏁 Getting Started

Follow these steps to get MyJournal running on your local machine.

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aman-Tomar-30/MyJournal-Flask.git
   cd MyJournal-Flask
   ```

2. **Create virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally

1. **Start the Flask development server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   ```
   http://localhost:5000
   ```

3. **Create an account and start journaling!** 📝

---

## 🌐 Deployment

MyJournal is production-ready and can be deployed to Render in minutes.

### Quick Deploy to Render

1. **Fork/Clone this repository**

2. **Sign up on [Render](https://render.com)** (free account)

3. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `myjournal` repo

4. **Configure Settings**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free

5. **Set Environment Variables**
```
   SECRET_KEY=<click-generate-button>
   ADMIN_USERNAME=<your-admin-username>
   ADMIN_PASSWORD=<your-secure-password>
   DATABASE_URL = <supabase-url>
```

6. **Click "Create Web Service"**

7. **Done!** Your app will be live in 2-3 minutes 🚀

### Environment Variables Explained

- `SECRET_KEY` - Flask session security (click "Generate" in Render)
- `ADMIN_USERNAME` - Your custom admin username (don't use "admin")
- `ADMIN_PASSWORD` - Strong password for admin panel (12+ characters)
- `DATABASE_URL` -  Supabase's PostgreSQL Database URL (defaults to SQLite)

### Post-Deployment

After deployment:
- Visit your live URL
- Create a user account
- Access admin panel at `/admin/login`
- Change admin credentials from defaults!

### Troubleshooting

**Build fails?**
- Check `requirements.txt` has all dependencies
- Verify Python version compatibility

**Database errors?**
- SQLite is used by default
- Database auto-creates on first run

**Admin login fails?**
- Verify environment variables are set
- Check for typos in username/password

---

## 💡 Usage

### For Users

1. **Sign Up**
   - Visit the homepage
   - Click "Get Started"
   - Fill in your details
   - Create your account

2. **Write Your First Entry**
   - Click "New Entry" from dashboard
   - Add a title and content
   - Save your entry

3. **Manage Entries**
   - View all your entries on the dashboard
   - Click "Read More" to view full entry
   - Edit or delete entries as needed


### For Admins

Access the admin panel at: `/admin/login`

**Default Credentials (Change in production!):**
- Username: `admin`
- Password: `admin123`

**Admin Features:**
- View user statistics
- Monitor all entries
- Track user activity
- View detailed analytics

---

## 🛡️ Admin Panel

The admin dashboard provides comprehensive monitoring and management capabilities.

### Access
```
URL: https://myjournal-9h9n.onrender.com/admin/login
Credentials: Set via environment variables
```

### Features

**Dashboard** (`/admin/dashboard`)
- Total users and entries
- Today's activity
- Recent users feed
- Recent entries
- Most active users leaderboard

**Users** (`/admin/users`)
- View all registered users
- User statistics
- Entry counts
- Profile details

**Entries** (`/admin/entries`)
- View all journal entries
- Entry statistics
- Word count analysis
- Full entry preview

**User Details** (`/admin/user/<id>`)
- Complete user profile
- All user's entries
- Activity statistics
- Writing analytics

---

## 📁 Project Structure

```
MyJournal-Flask/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── render.yaml                # Render deployment config
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── DEPLOYMENT_GUIDE.md        # Detailed deployment guide
├── LICENSE                    # MIT License
│
├── templates/                 # HTML templates
│   ├── index.html            # Homepage
│   ├── dashboard.html        # User dashboard
│   ├── create_entry.html     # Create journal entry
│   ├── view_entry.html       # View single entry
│   ├── edit_entry.html       # Edit entry
│   ├── contact.html          # Contact page
│   ├── about.html            # About page
│   ├── admin_login.html      # Admin login
│   ├── admin_dashboard.html  # Admin dashboard
│   ├── admin_users.html      # User management
│   ├── admin_entries.html    # Entry management
│   └── admin_user_detail.html # User details
│
└── instance/                  # Instance folder (auto-created If Supabase URL not Found)(Includes in .gitignore) 
    └── myjournal.db          # SQLite database
```

---

## 🔌 API Routes

### Public Routes
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Homepage |
| POST | `/signup` | User registration |
| POST | `/login` | User login |
| GET | `/logout` | User logout |
| GET | `/contact` | Contact page |
| GET | `/about` | About page |

### Protected User Routes (Login Required)
| Method | Route | Description |
|--------|-------|-------------|
| GET | `/dashboard` | User dashboard |
| GET/POST | `/create-entry` | Create journal entry |
| GET | `/entry/<id>` | View entry |
| GET/POST | `/edit-entry/<id>` | Edit entry |
| POST | `/delete-entry/<id>` | Delete entry |

### Admin Routes (Admin Login Required)
| Method | Route | Description |
|--------|-------|-------------|
| GET/POST | `/admin/login` | Admin login |
| GET | `/admin/logout` | Admin logout |
| GET | `/admin/dashboard` | Admin dashboard |
| GET | `/admin/users` | User management |
| GET | `/admin/entries` | Entry management |
| GET | `/admin/user/<id>` | User details |

---

## 🔐 Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Flask secret key for sessions | `your-secret-key-here` |
| `ADMIN_USERNAME` | Admin panel username | `admin` |
| `ADMIN_PASSWORD` | Admin panel password | `secure-password-123` |

### Optional Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Supabase connection URL | `sqlite:///myjournal.db` |
| `FLASK_ENV` | Flask environment | `production` |
| `PYTHON_VERSION` | Python version for Render | `3.11.0` |


### Production (Render Dashboard)
Set these in Render's environment variables section:
- `SECRET_KEY` - Click "Generate" for secure random key
- `ADMIN_USERNAME` - Your custom admin username
- `ADMIN_PASSWORD` - Strong password (12+ characters)

---

## 🤝 Contributing

Contributions are what make the open-source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write clear, descriptive commit messages
- Update documentation for any new features
- Test your changes thoroughly
- Keep pull requests focused on a single feature/fix

---

## 📄 License

Distributed under the MIT License. See `LICENSE` file for more information.

---

## 👨‍💻 Contact

**Aman Tomar**
- 💼 LinkedIn: [linkedin.com/in/tomaraman](https://linkedin.com/in/tomaraman)
- 🐙 GitHub: [@aman-Tomar-30](https://github.com/aman-Tomar-30)

**Project Links:**
- 🔗 Live Demo: [https://myjournal-9h9n.onrender.com](https://myjournal-9h9n.onrender.com)
- 📁 Repository: [https://github.com/aman-Tomar-30/MyJournal-Flask](https://github.com/aman-Tomar-30/MyJournal-Flask)
- 🐛 Report Issues: [GitHub Issues](https://github.com/aman-Tomar-30/MyJournal-Flask/issues)

---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ by [Aman Tomar](https://github.com/aman-Tomar-30)**

</div>

---

## 📝 Notes

- Change default admin credentials in production
- Use strong passwords for security
- Keep environment variables secure
- Regular backups recommended
- Monitor logs for issues

---

**Happy Journaling! 📔✨**