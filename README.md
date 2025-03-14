# Django Project README

## Table of Contents

* [Project Overview](#project-overview)
* [Requirements](#requirements)
* [Installation](#installation)
* [Configuration](#configuration)
* [Database Configuration](#database-setup)
* [Run Migrations](#running-migrations)
* [Starting the Development Server](#starting-the-development-server)
* [Common Issues](#common-issues)
* [License](#license)

## Project Overview

## Requirements

Python 3.6 or higher
Django 3.x or higher
PostgreSQL
Other dependencies can be found in the requirements.txt file.

## Installation
Clone the Repository:

```bash
git clone https://github.com/SamanNaruee/hamrah_keshavarz.git  
cd hamrah_keshavarz
```
Set Up a Virtual Environment:
It is recommended to use a virtual environment to manage your project dependencies:

```bash
python3 -m venv env  
source env/bin/activate  # On Windows use `env\Scripts\activate`  
```
# Install Dependencies:
Install the necessary packages:

```bash
pip install -r requirements.txt  
```
## Configuration
## Database Configuration:
Ensure you have PostgreSQL installed and set up. Create a new database for the project:

```sql
CREATE DATABASE your_database_name;  
```
Set Environment Variables:
Update the database settings in settings.py or use environment variables to manage sensitive information like database passwords:

```python
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'your_database_name',  
        'USER': 'your_username',  # Replace with your PostgreSQL username  
        'PASSWORD': 'your_password',  # Update this with your actual password  
        'HOST': 'localhost',  # Or your actual PostgreSQL host  
        'PORT': '5432',  # Default PostgreSQL port  
    }  
}
```  
Database Setup
Create a Superuser:
Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser  
```
# Run Migrations:
Before starting the application, run the migrations to set up the database schema:

```bash
python manage.py makemigrations  
python manage.py migrate  
```
## Running the Development Server
To run the development server, use the following command:

```bash
python manage.py runserver  
```
You can access the application in your web browser at http://127.0.0.1:8000/.

## Common Issues
Database Errors: Ensure your database is correctly set up, and the PostgreSQL service is running.

Permission Issues: If you encounter permissions errors (e.g., "permission denied for schema public"), ensure your PostgreSQL user has appropriate privileges. You can grant necessary permissions using:

```sql
GRANT ALL PRIVILEGES ON SCHEMA public TO your_username;  
```
Password Issues: If you encounter login errors related to the PostgreSQL user, double-check your password.

Migration Issues: When moving models between apps, ensure migrations are appropriately handled. You might need to delete old migration files and recreate them.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



