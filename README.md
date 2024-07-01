# Task Management System

This is a simple Task Management System built with Django and Django REST Framework. It allows users to create, read, update, 
and delete tasks, as well as fetch tasks based on their status (In Progress, Completed, Overdue).

## Features

- CRUD operations for tasks
- API endpoints to fetch tasks based on their status
- Responsive UI with Tailwind CSS

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (recommended)

## Installation

### 1. Clone the repository

Clone the repository to your local machine using the following command:

```sh
git clone https://github.com/yourusername/task_manager.git
cd task_manager

### **2. Install the required packages**
       use pipenv install or pip
          pip install -r requirements.txt

### 3. Activate the virtual environment
        use pipenv shell
### 4. Create and apply migrations
      use python manage.py makemigrations
          python manage.py migrate
### 5. Create a superuser
      use python manage.py createsuperuser
### 6. Run the development server
      use python manage.py runserver
7. Access the application
    Admin Interface: You can access the Django admin interface at http://127.0.0.1:8000/admin to manage tasks and users.

    API Endpoints:
All tasks: http://127.0.0.1:8000/api/tasks/
In progress tasks: http://127.0.0.1:8000/api/tasks/in_progress/
Completed tasks: http://127.0.0.1:8000/api/tasks/completed/
Overdue tasks: http://127.0.0.1:8000/api/tasks/overdue/

Contributions are welcome



