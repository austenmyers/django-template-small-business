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
    - <code>django-admin startproject --template https://github.com/austenmyers/django-template-small-business/archive/refs/tags/v0.2.2.zip |project_name| .</code>
    - <code>pip install -r requirements.txt</code>
    - create <code>.env</code> with:
        - <code>DEBUG=True</code>
        - <code>SECRET_KEY=some_string</code>
        - <code>DATABASE_URL=sqlite:///db.sqlite3</code>

- Updating Template
    - change |project_name| to {{ project_name }} in:
        - asgi.py
        - wsgi.py
        - settings/base.py (x2)
        - manage.py
    - push to https://github.com/austenmyers/django-template-small-business
    - update this readme with new version number
    - create new release
