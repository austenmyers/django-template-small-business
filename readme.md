# Django Project Template

## Description

+ Reformats <code>settings.py</code> as a python module with local environment variables.
+ Sets template, static, and media urls.
+ Creates apps in project_apps directory.
+ Includes home screen application.

## Requirements

- django
- django-environ

## Usage

- In a directory:
    - <code>py -m venv venv</code>
    - <code>.\venv\Scripts\activate</code>
    - <code>pip install django</code>
    - <code>django-admin startproject --template https://github.com/austenmyers/django-template-env/archive/refs/tags/v1.0.3.zip |project_name| .</code>
    - <code>pip install -r requirements.txt</code>
    - create <code>.env</code> with:
        - <code>DEBUG=True</code>
        - <code>SECRET_KEY=some_string</code>
        - <code>DATABASE_URL=sqlite:///db.sqlite3</code>

- Creating an app:
    - <code>mkdir project_apps/'app_name'</code>
    - <code>python manage.py startapp |app_name| project_apps/|app_name|</code>
    - <code>INSTALLED_APPS += ['project_apps.|app_name|']</code>
    - Update <code>|app_name|/apps.py |App_Name|Config.name = 'project_apps.|app_name|'</code> 
