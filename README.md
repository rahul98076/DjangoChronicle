# Full-Stack Django Blog Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-darkgreen?logo=django&logoColor=white)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

A full-featured blog application built with the Django framework. This project was built to demonstrate core web development skills, including backend logic, database management, and professional deployment practices using Docker.

## Key Features 🚀

- Developed a dynamic content platform with post creation and a full admin moderation panel.
- Engineered an interactive comment system with an approval queue for user-submitted content.
- Containerized the application using **Docker**, configured a production-ready server with **Gunicorn**, and managed static files with **WhiteNoise**.
- Ensured code quality and security with a professional toolchain, including automated testing, linting (Flake8), and auto-formatting (Black).

## Tech Stack 🛠️

- **Backend:** Python, Django, Gunicorn
- **Frontend:** HTML, CSS
- **Database:** SQLite3
- **Containerization:** Docker
- **Testing & Tooling:** Flake8, Black, Git

## Local Development Setup 💻

There are two ways to run this project locally. Using Docker is the recommended method as it replicates the production environment perfectly.

### Option 1: Running with Docker (Recommended)

1.  **Prerequisites:** Make sure you have Docker Desktop installed and running.
2.  **Clone the repository:** `git clone https://github.com/rahul98076/DjangoChronicle.git`
3.  **Create the environment file:** Create a new file named `.env` and copy the contents of `.env.example` into it. Generate a new Django `SECRET_KEY`.
4.  **Build the Docker image:** `docker build -t your-repo-name .`
5.  **Run the Docker container:** `docker run --env-file .env -p 8000:8000 your-repo-name`

### Option 2: Running with a Virtual Environment (Classic)

1.  **Clone the repository:** `git clone https://github.com/rahul98076/DjangoChronicle.git`
2.  **Create and activate a virtual environment:** `py -m venv venv` and `.\venv\Scripts\activate`
3.  **Install dependencies:** `pip install -r requirements.txt`
4.  **Create the environment file:** Create `.env` from `.env.example` and set your `SECRET_KEY`.
5.  **Run migrations and create a superuser:** `py manage.py migrate` and `py manage.py createsuperuser`
6.  **Run the development server:** `py manage.py runserver`

The application will be available at `http://127.0.0.1:8000/`.

## Running Tests

To run the automated tests, use the following command:

`py manage.py test`
