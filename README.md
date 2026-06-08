# Flask Authentication & Task Manager

A full-stack web application built using Flask, MySQL, JavaScript, HTML, and CSS. The application provides secure user authentication and a user-specific task management system with complete CRUD functionality.

## Features

### Authentication System

* User Registration
* User Login
* Password Hashing using Werkzeug Security
* Session Management
* Protected Routes
* Logout Functionality

### Task Management

* Create Tasks
* View Tasks
* Update Tasks
* Delete Tasks
* User-Specific Tasks
* Dynamic UI Updates using Fetch API

## Technologies Used

### Backend

* Python
* Flask
* MySQL
* mysql.connector

### Frontend

* HTML
* CSS
* JavaScript
* Fetch API

### Security

* Password Hashing
* Session-Based Authentication

## Project Structure

```text
flask-auth-project/
│
├── app.py
├── database.py
├── decorators.py
├── routes/
├── templates/
├── static/
│   ├── css/
│   └── js/
├── README.md
└── requirements.txt
```

## Installation

### Clone Repository

```bash
git clone https://github.com/dominic-rozario1210/flask-auth-project.git
```

### Navigate to Project

```bash
cd flask-auth-project
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install flask
pip install mysql-connector-python
```

### Configure MySQL Database

Create the required database and tables in MySQL.

### Run Application

```bash
python app.py
```

## Learning Outcomes

Through this project, I learned:

* Flask Routing
* Template Inheritance
* Blueprints
* Session Management
* Password Hashing
* MySQL Database Integration
* REST-style JSON APIs
* JavaScript Fetch API
* CRUD Operations
* Git & GitHub Workflow

## Future Improvements

* Deployment to Cloud Platform
* User Profile Management

## Author

Dominic Rozario E
B.Sc Mathematics | M.Sc Mathematics
Aspiring Backend Developer
