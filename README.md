🏢 Django Recruitment Portal

A full-featured recruitment management system built with Django, designed to streamline the hiring process for companies and provide an easy-to-use portal for job seekers.

✨ Features
👩‍💼 For Employers / Admins

Secure authentication and role-based access control

Post, update, and delete job listings

Manage candidate applications and shortlisting

Search and filter candidates by skills, experience, or status

Dashboard with analytics on job postings and applications

👨‍💻 For Job Seekers

Create and update profiles with resume upload

Browse and apply to job postings

Track application status in real-time

Email notifications for application updates

⚙️ Core System Features

Django ORM with PostgreSQL support

Responsive Bootstrap frontend (mobile-friendly)

RESTful API endpoints for integrations (

Role-based dashboards (Admin / Recruiter / Candidate)

🛠️ Tech Stack

Backend: Django (Python 3.x)

Frontend: Bootstrap / Tailwind (if applicable)

Database: PostgreSQL / MySQL / SQLite (choose based on setup)

Authentication: Django Auth (with optional social login)

Deployment: Gunicorn + Nginx / Docker / Any cloud platform (Render, Railway, DigitalOcean, Heroku, etc.)

🚀 Getting Started
1. Clone the repo
git clone https://github.com/yourusername/recruitment-portal.git
cd recruitment-portal

2. Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Setup environment variables

Create a .env file in the project root with the following:

SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/recruitment_db
EMAIL_HOST=smtp.example.com
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_password

4. Run migrations & start server
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Your app will be live at 👉 http://127.0.0.1:8000

📸 Screenshots (Optional)

Add some UI screenshots here to showcase login, dashboards, job listings, etc.

📦 Deployment

Docker:

docker build -t recruitment-portal .
docker run -p 8000:8000 recruitment-portal


Or deploy easily on Heroku / Railway / Render / DigitalOcean.

🤝 Contributing

Contributions are welcome! Please fork this repo and submit a pull request.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by [Your Name] 🚀

Portfolio: yourportfolio.com

LinkedIn: linkedin.com/in/yourprofile
