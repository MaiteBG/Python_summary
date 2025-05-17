<!-- TOC -->
  * [1. Creating a Django Project](#1-creating-a-django-project)
    * [1.1. Project Structure Description](#11-project-structure-description)
    * [1.2. Running the Development Server](#12-running-the-development-server)
  * [2. App in Django](#2-app-in-django)
    * [2.1. Creating a New App](#21-creating-a-new-app)
  * [3. MTV (Model-Template-View) architectural](#3-mtv-model-template-view-architectural)
  * [4. "Controller" in Django (Views)](#4-controller-in-django-views)
    * [4.1. Create a view](#41-create-a-view)
    * [4.2. Add a URL Pattern in Django](#42-add-a-url-pattern-in-django)
  * [5. Model and model class](#5-model-and-model-class)
    * [5.1. Databases connection](#51-databases-connection)
    * [5.2. Migrations](#52-migrations)
  * [6. Model class](#6-model-class)
<!-- TOC -->

## 1. Creating a Django Project

To create a new Django project, run the following command in your terminal:

```bash
django-admin startproject project_name
```

Replace `project_name` with your desired project folder name.

### 1.1. Project Structure Description

After running the command, Django generates a directory structure like this:

```
project_name/
├── manage.py
└── project_name/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

- **manage.py**: Utility script for managing the project (runserver, migrations, etc.).
- **project_name/**: Inner directory containing project settings and configuration.
  - **__init__.py**: Marks the directory as a Python package.
  - **settings.py**: Main configuration file for the project.
  - **urls.py**: URL declarations for the project.
  - **asgi.py**: Entry point for ASGI-compatible web servers.
  - **wsgi.py**: Entry point for WSGI-compatible web servers.

This structure separates project-level configuration from application code, making it easy to manage and scale your Django project.


### 1.2. Running the Development Server

> **Note:** All `python manage.py` commands must be run from the project root directory. 
> If you are using PyCharm, right-click your project folder and select **"Mark Directory as > Sources Root"** to set the correct working directory.


To start the Django development server and see your project in action, use the following command inside your project directory:


```bash
python manage.py runserver
```

You can also specify a port (for example, 8080) with:

```bash
python manage.py runserver 8080
```


This will launch a local web server, usually accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). You can now view your Django project in your web browser.

To stop the development server, return to your terminal and press `Ctrl+C`.



> **Note:** When you create and run a Django project for the first time, a `db.sqlite3` file is automatically generated. This file is Django's default database and stores all the project's data.
> If you want to use a different database (such as PostgreSQL or MySQL), you can configure it in the `DATABASES` section of your project's `settings.py` file.



## 2. App in Django

In Django, an **app** is a modular component that handles a specific functionality of your project. Each app is a Python package that can be reused in different projects. For example, you might have separate apps for user authentication, blog posts, or comments.

### 2.1. Creating a New App

To create a new app in your Django project, run the following command inside your project directory:

```bash
python manage.py startapp app_name
```

Replace `app_name` with the desired name for your app.

This command creates a directory structure like:

```
appname/
├── migrations/        # Database migrations for this app
│   └── __init__.py
├── __init__.py        # Marks this directory as a Python package
├── admin.py           # Register models for the admin interface
├── apps.py            # App configuration
├── models.py          # Define your data models here
├── tests.py           # Write tests for your app here
└── views.py           # Handle requests and return responses
```

After creating a new app (for example, `myapp`), you must register it so Django recognizes it as part of your project. Add it to the `INSTALLED_APPS` list in your project's `settings.py` file so Django recognizes it.


> **Note:**  Registering your app is required for Django to detect models, admin settings, and other app-specific configurations.


```python
INSTALLED_APPS = [
    # ... existing apps ...
    'myapp',  # Add this line for your new app
]
```

## 3. MTV (Model-Template-View) architectural

Django uses the MTV (Model-Template-View) architectural pattern:

- **Model**: Defines your data structure and business logic. Models map to database tables and handle data manipulation.
- **Template**: Responsible for rendering the HTML and presenting data to the user.
- **View**: Contains the logic to process requests, interact with models, and return responses (often rendering templates).

This separation helps organize code, making it easier to maintain and scale Django projects.

> **Note:**  
> The MTV (Model-Template-View) pattern in Django is similar to the MVC (Model-View-Controller) pattern used in other frameworks.  
> - In Django, the "View" corresponds to the "Controller" in MVC, handling request logic.  
> - The "Template" in MTV is like the "View" in MVC, responsible for presentation.  
> - The "Model" serves the same purpose in both patterns, managing data and business logic.  
>  
> This naming difference reflects Django’s design choices, but the core architectural concepts are very similar.
> 
> | Component     | **MVC (Model-View-Controller)**                                                                          | **MVT (Model-View-Template)**                                                                              |
> | ------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
> | **Model**     | Represents the data and business logic.                                                                  | Identical: represents the data and business logic.                                                         |
> | **View**      | What the user sees (HTML, CSS).                                                                          | In Django, the *View* is the logic that handles the request, **not** the HTML template.                    |
> | **Controller**| Handles the control logic (responds to user input, invokes the model, selects the view).                 | Equivalent to Django’s *View* (functions or classes that receive requests and return responses).           |
> | **Template**  | Does not exist as a separate component. HTML is integrated into the view.                                | Is the HTML file with presentation logic (use of template tags, loops, conditions, etc.).                  |
> 



## 4. "Controller" in Django (Views)
In Django, the "controller" logic is handled by **views**. Views are Python functions or classes that receive web requests and return web responses. They process input, interact with models, and delegate rendering to templates.

A user’s browser sends an HTTP request to the Django server, which creates an `HttpRequest` object. The view processes this and returns an `HttpResponse`, which Django sends back to the browser. This request-response cycle repeats as the user interacts with the site.

- **Request Object:**  
    Every view receives an `HttpRequest` object as its first argument, containing metadata about the request (like GET/POST data, headers, user info, etc.).

- **Response Object:**  
    Views return an `HttpResponse` object (or subclasses like `JsonResponse`). This object contains the content, status code, and headers to send back to the client.
```
 (---HttpRequest object--->)
User ⇄ Django Serverm ⇄ View
 (<---HttpResponse object---)   
```

### 4.1. Create a view

On `views.py` from any of your app. 

```python
from django.http import HttpResponse

def my_view(request):
        return HttpResponse("Hello, world!")
```

- **Accessing Request Data:**  
    - `request.GET` for query parameters (URL data)
    - `request.POST` for form data
    - `request.user` for the authenticated user

    Example: This view reads a `name` parameter from the URL and returns a personalized greeting.

    ```python
    from django.http import HttpResponse

    def greet_user(request):
            name = request.GET.get('name', 'Guest')
            return HttpResponse(f"Hello, {name}!")
    ```

***View Classes:**  Django also supports class-based views for more complex logic and reusability.*

### 4.2. Add a URL Pattern in Django

To make a view accessible via a browser, you need to add a URL pattern in your app’s `urls.py` file. This maps a specific URL path to a view function or class.

**Include your app’s URLs in the project’s main `urls.py`:**

```python
from django.urls import path
from your_app.views import my_view

urlpatterns = [
    path('your-url/', my_view),
]
```

- `'your-url/'` is the URL path.  
  - If `''` is the URL path it corresponds to the main page (default page) when the URL is empty.
- `my_view` is the view function to handle requests to this URL.
- `name` is an optional identifier used for reverse URL resolution.
  - For example, `name='index'` can be used to refer to the main page (useful for redirects).
  - In an HTML template, you can use: `<a href="{% url 'index' %}">`.
  - It's a good practice to use `name` because if the URL path changes, you won't need to update the links throughout your code.

Now, visiting `/your-url/` in your browser will trigger `your_view` and display the response.




## 5. Model and model class

### 5.1. Databases connection

By default, Django projects are configured to use SQLite, which creates a `db.sqlite3` file in your project directory after running the server or applying migrations. SQLite is simple and requires no additional setup, making it ideal for development and small projects.

However, Django also supports other databases like PostgreSQL. To use PostgreSQL, update the `DATABASES` setting in your project's `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Make sure you have the `psycopg2` package installed.

### 5.2. Migrations

After configuring your database, Django uses a system called migrations to manage changes to your database schema.

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They are like version control for your database, allowing you to evolve your database structure over time in a consistent and easy way.

To see which migrations are available and their status, use:

```bash
python manage.py showmigrations
```

This command lists all migrations for each app and shows which ones have been applied.

To apply migrations (i.e., update your database schema to match your models), run:

```bash
python manage.py migrate
```

This command will create the necessary tables and apply any pending changes to your database.



## 6. Model class

A model in Django is a Python class that defines the structure of your database tables. Each model maps to a single table in the database.

To create a model, open the `models.py` file inside your app directory and define a class that inherits from `django.db.models.Model`. For example:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
```

After defining your model, you need to create and apply migrations to update the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

> **Note:** These commands must be run inside your project directory.

Once migrated, Django will create the corresponding table in your database (e.g., `db.sqlite3` by default).

To use your model in the Django admin interface, register it in `admin.py`:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

This allows you to add, edit, and delete records for your model through the admin site.