# Simple Blog Engine in Django

This is a simple blog application built with the Django framework. It includes features like post creation, a comment system with moderation, and a full admin panel. This project was built to demonstrate core web development skills in Python and Django.

## Features

- Create, display, and manage blog posts.
- Comment system with admin approval.
- Professional setup including code formatting (Black), linting (Flake8), and automated tests.
- Secure key management using environment variables.

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    `git clone <your-repository-url>`

2.  **Navigate to the project directory:**
    `cd simple_blog`

3.  **Create and activate a virtual environment:**
    `py -m venv venv`
    `.\venv\Scripts\activate`

4.  **Install the dependencies:**
    `pip install -r requirements.txt`

5.  **Create the environment file:**
    Create a new file named `.env` in the root of the project. Copy the contents of `.env.example` into it and generate a new secret key.
    `SECRET_KEY='your-new-super-secret-key'`

6.  **Run database migrations:**
    `py manage.py migrate`

7.  **Create a superuser to access the admin panel:**
    `py manage.py createsuperuser`
    (Follow the prompts to create your admin account)

8.  **Run the development server:**
    `py manage.py runserver`

The blog will now be running at `http://127.0.0.1:8000/`. You can access the admin panel at `http://127.0.0.1:8000/admin/`.
