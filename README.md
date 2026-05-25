# 🎓 Examify

> A full-stack online examination portal with subject-wise MCQ tests, question management, user roles, and real-time scoring — built with Django.

---

## 🚧 Work In Progress

> ⚠️ **This project is currently under active development.**
> Core features are working. More improvements and pages are being added regularly!

---

## 📌 About

**Examify** (also called **ExamFusion** in the UI) is a web-based exam portal built with Django. It supports multiple roles (Admin, Teacher, Student), lets admins manage questions and users, and allows students to take subject-wise MCQ tests and instantly see their score.

---

## 📸 Modules -

### 🔐 Login Page
Users log in with a username and password on a clean dark-themed login screen.

### 🏠 Home / Dashboard
After login, the home page shows three main modules — **Question Module**, **User Module**, and **Start Test**.

### 📋 Question Management
Full CRUD for exam questions:
- **Add Question** — Enter question text, 4 options, correct answer, and subject
- **View Questions** — Table showing all questions with subject and correct answer
- **Update Questions** — Edit existing questions
- **Delete Questions** — Remove unwanted questions

### 👥 User Management
Admin can **add, edit, and delete** users. Each user has a username, email, and role (Admin / Teacher / Student).

### 📚 Subject Selection
Students pick a subject before starting the test. Currently available subjects: **Python, HTML, CSS, SQL**

### 📝 Test / Exam Page
MCQ-based exam with Previous / Next navigation and an **End Exam** button. Shows question number progress (e.g. Question 1 / 2).

### 🏁 Result Page
After ending the exam, students instantly see their **final score** (e.g. 0 / 2) with an option to **Start New Test**.

---

## ✨ Features

- 🔐 **User Authentication** — Secure login system
- 👥 **User Management** — Add / Edit / Delete users with role assignment (Admin, Teacher, Student)
- 📋 **Question CRUD** — Create, view, update, and delete exam questions per subject
- 📚 **Subject Selection** — Choose from Python, HTML, CSS, SQL before taking a test
- 📝 **MCQ Exam** — Navigate questions with Previous / Next, end exam anytime
- 📊 **Instant Results** — Score displayed immediately after exam ends
- 🌐 **Multi-language Ready** — Google Translate integration visible in UI

---

## 🗂️ Project Structure

```
Examify/
├── Examapp/                  # Main Django app
│   ├── models.py             # Question, User models
│   ├── views.py              # All page logic
│   └── urls.py               # App URL routes
├── Examproject/              # Django project config
│   ├── settings.py
│   └── urls.py
├── static/
│   └── css/
│       └── style.css         # Master stylesheet (dark theme)
├── subject.html              # Subject selection page
├── manage.py                 # Django entry point
└── README.md
```

---

## 🌐 Pages & URLs

| Page | URL |
|------|-----|
| Login | `/examapp/loginuser/` |
| Home | `/examapp/` |
| Question Management | `/examapp/questioncurd/` |
| Add Question | `/examapp/create-question/` |
| View Questions | `/examapp/show-questions/` |
| User Management | `/examapp/userdashboard/` |
| Select Subject | `/examapp/subject/` |
| Take Test | `/examapp/next-question/` |
| Result | `/examapp/end-test/` |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

Open **http://127.0.0.1:8000/examapp/loginuser/** in your browser.

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Django          |
| Frontend   | HTML, CSS               |
| Database   | MySQL                   |
| Styling    | Custom CSS (Dark Theme) |

---

## 🗺️ Roadmap

- [x] User login system
- [x] Question CRUD (Add, View, Update, Delete)
- [x] User management with roles
- [x] Subject selection (Python, HTML, CSS, SQL)
- [x] MCQ exam with navigation
- [x] Instant result/score display
- [ ] Apply new CSS redesign to all pages
- [ ] Timer for each exam
- [ ] Student-specific exam history
- [ ] Performance analytics and charts
- [ ] Export results as PDF
- [ ] Mobile responsive design
- [ ] Deploy to live server

---

## 👨‍💻 Author

**Teja** — [@teja3101](https://github.com/teja3101)
