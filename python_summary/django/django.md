
<!-- TOC -->
  * [1. Creating a Django Project](#1-creating-a-django-project)
    * [1.1. Project Structure Description](#11-project-structure-description)
    * [1.2. Running the Development Server](#12-running-the-development-server)
  * [2. App in Django](#2-app-in-django)
    * [2.1. Creating a New App](#21-creating-a-new-app)
  * [3. MTV (Model-Template-View) architectural](#3-mtv-model-template-view-architectural)
  * [4. Databases, model class and model form class](#4-databases-model-class-and-model-form-class)
    * [4.1. Databases](#41-databases)
      * [4.1.1. Migrations](#411-migrations)
    * [4.2. Model Class](#42-model-class)
      * [4.2.1. `Field()` Methods](#421-field-methods)
      * [4.2.2. Primary Key in Django Models](#422-primary-key-in-django-models)
      * [4.2.3. Defining Relationships Between Models](#423-defining-relationships-between-models)
      * [4.2.4. Applying Model Changes](#424-applying-model-changes)
    * [4.3. ModelForm](#43-modelform)
  * [5. Django Admin](#5-django-admin)
    * [5.1. Creating a Superuser](#51-creating-a-superuser)
    * [5.2. Registering Models with Admin](#52-registering-models-with-admin)
    * [5.3. Customizing Object Display](#53-customizing-object-display)
  * [6. Views in Django ("Controller")](#6-views-in-django-controller)
    * [6.1. Add a URL Pattern](#61-add-a-url-pattern)
      * [6.1.1. Including Parameters in URL Patterns](#611-including-parameters-in-url-patterns)
    * [6.2. View method to templates: `render()`](#62-view-method-to-templates-render)
  * [7. Templates](#7-templates)
    * [7.1. Basic strucutre for HTML templates](#71-basic-strucutre-for-html-templates)
  * [8. Using Model Classes in Views and Templates](#8-using-model-classes-in-views-and-templates)
    * [8.1. Accessing Model Data in Views](#81-accessing-model-data-in-views)
    * [8.2. Using Model Data in Templates](#82-using-model-data-in-templates)
    * [8.3. Detail View Example](#83-detail-view-example)
  * [9. Using ModelForm Class in Views and Templates](#9-using-modelform-class-in-views-and-templates)
    * [9.1. Interaccion with database](#91-interaccion-with-database)
    * [9.2. CSRF Protection in Django Forms](#92-csrf-protection-in-django-forms)
    * [9.3. Basic Workflow](#93-basic-workflow)
    * [9.4. Editing and Deleting Objects](#94-editing-and-deleting-objects)
<!-- TOC -->

## 1. Creating a Django Project

To create a new Django project, run the following command in your terminal:

```bash
django-admin startproject project_name
```

Replace `project_name` with your desired project name.

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
- **project_name/**: Inner directory containing the main project configuration.
    - **\_\_init\_\_.py**: Marks the directory as a Python package.
    - **settings.py**: Main configuration file for the project.
    - **urls.py**: URL declarations for the project.
    - **asgi.py**: Entry point for ASGI-compatible web servers.
    - **wsgi.py**: Entry point for WSGI-compatible web servers.
    - 
This structure separates project-level configuration from application code, making it easy to manage and scale your Django project.

### 1.2. Running the Development Server

> **Note:** All `python manage.py` commands must be run from the project root directory.  
> If you are using PyCharm, right-click your project folder and select **"Mark Directory as > Sources Root"** to set the correct working directory.

To start the Django development server and view your project in action, run the following command from your project directory:

```bash
python manage.py runserver
```

To specify a different port (for example, 8080), use:

```bash
python manage.py runserver 8080
```

This launches a local web server, typically accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Open this address in your web browser to see your Django project.

To stop the development server, press `Ctrl+C` in your terminal.

> **Note:** When you run a Django project for the first time, a `db.sqlite3` file is automatically created.  
> This is Django's default database, used to store all project data.  
> To use a different database (such as PostgreSQL or MySQL), update the `DATABASES` section in your project's `settings.py` file.

## 2. App in Django

In Django, an **app** is a modular component that encapsulates a specific functionality within your project. Each app is a Python package that can be reused across different projects. For example, you might create separate apps for user authentication, blog posts, or comments.

### 2.1. Creating a New App

To create a new app in your Django project, run the following command from your project directory:

```bash
python manage.py startapp app_name
```

Replace `app_name` with your desired app name.

This command generates the following directory structure:

```
app_name/
├── migrations/        # Database migrations for this app
│   └── __init__.py
├── __init__.py        # Marks this directory as a Python package
├── admin.py           # Register models for the admin interface
├── apps.py            # App configuration
├── models.py          # Define your data models here
├── tests.py           # Write tests for your app here
└── views.py           # Handle requests and return responses
```

After creating a new app (for example, `myapp`), you must register it so Django recognizes it as part of your project. Add it to the `INSTALLED_APPS` list in your project's `settings.py` file:

> **Note:** Registering your app is required for Django to detect models, admin settings, and other app-specific configurations.

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
- **View**: Contains the logic to process requests, interact with models, and return responses (often rendering
  templates).

This separation helps organize code, making it easier to maintain and scale Django projects.

> **Note:**  
> The MTV (Model-Template-View) pattern in Django is similar to the MVC (Model-View-Controller) pattern used in other
> frameworks.
>
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

## 4. Databases, model class and model form class

### 4.1. Databases

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

#### 4.1.1. Migrations

**Migrations** are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They act as a version control system for your database, allowing you to evolve your schema safely and consistently as your project grows.

**Key migration commands:**

- `python manage.py makemigrations`  
    Scans your models for changes and creates new migration files in the `migrations/` directory of each app. These files describe the operations needed to update your database schema.

- `python manage.py migrate`  
    Applies all pending migrations to your database, creating or altering tables and fields as needed.

- `python manage.py showmigrations`  
    Lists all migrations and shows which ones have been applied.

- `python manage.py sqlmigrate app_name migration_number`  
    Shows the raw SQL that Django will run for a given migration. Useful for understanding exactly what changes will be made to the database.  
    Example: `python manage.py sqlmigrate myapp 0001`

**Typical workflow:**

1. Make changes to your models (add, modify, or remove fields/classes).
2. Run `makemigrations` to generate migration files.
3. Run `migrate` to apply those changes to your database.

**Best practices:**

- Always run `makemigrations` and `migrate` after modifying your models.
- Keep migration files under version control (e.g., Git) to track schema changes.
- Review migration files before applying them, especially in production environments.

For more details, see the [official Django migrations documentation](https://docs.djangoproject.com/en/stable/topics/migrations/).

### 4.2. Model Class

A **model class** in Django is a Python class that defines the structure and behavior of a database table. Each model maps to a single table, and each attribute of the class represents a column (field) in that table. Models are defined by subclassing `django.db.models.Model`.

- Define fields using Django’s built-in field types (e.g., `CharField`, `IntegerField`, `DateField`, `ForeignKey`).
- Automatically generate database tables and columns based on your model definitions.
- Provide a high-level Pythonic API for creating, querying, updating, and deleting records.
- Support relationships between tables (one-to-many, many-to-many, one-to-one).

**Meta options:** You can customize model behavior using the inner `Meta` class (e.g., ordering, verbose names, unique constraints).

```python
class Book(models.Model):
    # fields...
    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
```


#### 4.2.1. `Field()` Methods

Django models use field classes to define the type and behavior of each database column. Each attribute in a model class is an instance of a subclass of `django.db.models.Field`. These fields handle data conversion, validation, and database mapping.

**Common field types:**

- `CharField(max_length=...)`: Short text fields (e.g., names, titles).
- `TextField()`: Large text fields (e.g., descriptions, comments).
- `IntegerField()`: Integer values.
- `FloatField()`: Floating-point numbers.
- `BooleanField()`: True/False values.
- `DateField()`, `DateTimeField()`: Dates and date-times.
- `EmailField()`: Email addresses.
- `URLField()`: URLs.
- `ForeignKey()`: Many-to-one relationships.
- `ManyToManyField()`: Many-to-many relationships.
- `OneToOneField()`: One-to-one relationships.

**Common field options:**

- `null`: If `True`, the field can be `NULL` in the database.
- `blank`: If `True`, the field can be left blank in forms.
- `default`: Sets a default value for the field.
- `choices`: Restricts the field to a set of predefined values.
- `unique`: If `True`, ensures all values in this field are unique.
- `verbose_name`: Human-readable name for the field.
- `help_text`: Extra help text for forms and admin.

**Example:**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, help_text="Enter the book title")
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    genre = models.CharField(
        max_length=20,
        choices=[
            ('fiction', 'Fiction'),
            ('nonfiction', 'Non-Fiction'),
            ('poetry', 'Poetry'),
        ],
        default='fiction'
    )
    is_published = models.BooleanField(default=False)
    description = models.TextField(blank=True)
```

For a full list of available fields and options, see the [official Django model field reference](https://docs.djangoproject.com/en/stable/ref/models/fields/).

#### 4.2.2. Primary Key in Django Models

In Django, every model requires a primary key—a unique identifier for each record in the database table. By default, Django automatically adds an `id` field to every model, which is an auto-incrementing integer (`AutoField`) and serves as the primary key. 
**Default behavior:**

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    # Django automatically adds: id = models.AutoField(primary_key=True)
```

**Custom primary key:**

If you want to use a different field as the primary key (for example, an ISBN or a UUID), you can define it explicitly by setting `primary_key=True` on that field. Only one field in a model can have this option. If you define your own primary key, Django will not add the default `id` field.

```python
class Book(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
```

For more details, see the [official Django model primary key documentation](https://docs.djangoproject.com/en/stable/topics/db/models/#automatic-primary-key-fields).

#### 4.2.3. Defining Relationships Between Models

Django provides several field types to define relationships between models, allowing you to represent complex data structures and associations in your database.

##### 4.2.3.1. ForeignKey (Many-to-One)

A `ForeignKey` creates a many-to-one relationship. For example, each book has one author, but an author can have many books.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```


> Choose `on_delete` behavior carefully to maintain data integrity.

- **`on_delete`**: Determines what happens when the referenced object is deleted.
    - `models.CASCADE`: Delete related objects (default).
    - `models.PROTECT`: Prevent deletion if related objects exist.
    - `models.SET_NULL`: Set the field to `NULL` (requires `null=True`).
    - `models.SET_DEFAULT`: Set to default value (requires `default=...`).
    - `models.SET(...)`: Set to a specific value or function.
    - `models.DO_NOTHING`: Do nothing (not recommended unless handled manually).

- Access all books by an author: `author.book_set.all()`

##### 4.2.3.2. OneToOneField (One-to-One)

A `OneToOneField` creates a one-to-one relationship. Each object of one model is related to one and only one object of another model. This is useful for extending user profiles or splitting model information.

```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

- Each `Profile` is linked to a unique `User`.
- Access the profile from the user: `user.profile`

##### 4.2.3.3. ManyToManyField (Many-to-Many)

A `ManyToManyField` creates a many-to-many relationship. Each object can relate to multiple objects of another model, and vice versa. For example, a book can have multiple genres, and a genre can belong to multiple books.

```python
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
```

- Access all genres of a book: `book.genres.all()`
- Access all books in a genre: `genre.book_set.all()`

For more details, see the [official Django model relationship documentation](https://docs.djangoproject.com/en/stable/topics/db/models/#relationships).


#### 4.2.4. Applying Model Changes

After defining your model, you need to create and apply migrations to update the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

Once migrated, Django will create/update the corresponding table in your database (e.g., `db.sqlite3` by default).


### 4.3. ModelForm
Forms in Django can be created manually or automatically using **ModelForm**. A ModelForm is a helper class that creates a form based on a Django model, mapping model fields to form fields automatically.

**Advantages of ModelForm:**

- Reduces repetitive code by generating forms directly from models.
- Ensures form fields stay in sync with model changes.
- Handles validation and saving of model instances.
- Easily customizable for layout and widgets.

**Basic usage:**
1. Create a form class in your app’s `forms.py`:
    ```python
    from django import forms
    from .models import Book

    class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = ['title', 'author', 'published_date']
    ```
    - `model`: The model to base the form on.
    - `fields`: List of model fields to include in the form. Use `'__all__'` to include all fields.

2. Use the form in your views to display, validate, and save data.

3. Render the form in your templates using `{{ form.as_p }}`, `{{ form.as_table }}`, or `{{ form.as_ul }}`.

**Customizing ModelForm:**

- You can specify widgets, labels, help texts, and validation rules in the `Meta` class or by overriding form methods.
- **Widgets** control how form fields are rendered in HTML (e.g., text input, textarea, date picker). The `attrs` dictionary lets you add HTML attributes (like CSS classes or placeholders).
- Example with widgets:

```python
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'genre', 'is_published', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book Title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author Name'
            }),
            'published_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-select'
            }),
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Short description of the book'
            }),
        }
```

**Common widgets used above:**

- `TextInput`: For single-line text fields (`title`, `author`)
- `DateInput`: For date selection (`published_date`)
- `Select`: For dropdown choices (`genre`)
- `CheckboxInput`: For boolean fields (`is_published`)
- `Textarea`: For multi-line text (`description`)

For more details, see the [official Django ModelForm documentation](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/).s in Django

## 5. Django Admin

Django includes a powerful built-in admin interface for managing your project's data at `admin/` URL. The admin site allows you to add, edit, and delete records for your models through a web interface.

### 5.1. Creating a Superuser

To access the admin site, you need a superuser account. Create one by running:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

Once created, start your development server and visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Log in with your superuser credentials.

### 5.2. Registering Models with Admin

To manage a model in the admin interface, register it in your app's `admin.py` file:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

After registering, the model will appear in the admin dashboard. This allows you to add, edit, and delete records for your model through the admin site.

### 5.3. Customizing Object Display

By default, Django displays each object in the admin as `ModelName object (id)`. To show more meaningful information, override the `__str__` method in your model:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author}"
```

The admin will now display each book using the string returned by `__str__`, making it easier to identify records.

## 6. Views in Django ("Controller")

In Django, the "controller" logic is handled by **views**. Views are Python functions or classes that receive web requests and return web responses. They process input, interact with models, and delegate rendering to templates.

> Django also supports class-based views for more complex logic and reusability.

A user’s browser sends an HTTP request to the Django server, which creates an `HttpRequest` object of `django.http` module. The view processes this and returns an `HttpResponse` object of `django.http` module, which Django sends back to the browser. This request-response cycle repeats as the user interacts with the site.

- **Request Object:** Every view receives an `HttpRequest` object as its first argument, containing metadata about the   request (like GET/POST data, headers, user info, etc.). View methods always recibe a `request` parameter as firts   argument.
    - `request.GET` for query parameters (URL data)
    - `request.POST` for form data
    - `request.user` for the authenticated user

- **Response Object:** Views return an `HttpResponse` object (or subclasses like `JsonResponse`). This object contains   the content, status code, and headers to send back to the client.

  ```
  (----HttpRequest object--->)
  User ⇄ Django Server ⇄ View
  (<---HttpResponse object---)   
  ```

On `views.py` from any of your app.

```python
from django.http import HttpResponse

def greet_user(request):
    '''
    This view reads a `name` parameter from the URL and returns a personalized greeting.
    '''
    name = request.GET.get('name', 'Guest')
    return HttpResponse(f"Hello, {name}!")
```

### 6.1. Add a URL Pattern

To make a view accessible via a browser, you need to add a URL pattern in your app’s `urls.py` file. This maps a specific URL path to a view function or class.

**Include your app’s URLs in the project’s main `urls.py`:**

```python
from django.urls import path
from your_app.views import my_view

urlpatterns = [
    path('your-url/', my_view, name='my_view'),
]
```

- `'your-url/'` is the URL path.
    - If `''` is the URL path it corresponds to the main page (default page) when the URL is empty.
- `my_view` is the view function to handle requests to this URL.
- `name` is an optional identifier used for reverse URL resolution.
    - For example, `name='index'` can be used to refer to the main page (useful for redirects).
    - In an HTML template, you can use: `<a href="{% url 'index' %}">`.
    - It's a good practice to use `name` because if the URL path changes, you won't need to update the links throughout your code.

Now, visiting `/your-url/` in your browser will trigger `my_view` and display the response.

#### 6.1.1. Including Parameters in URL Patterns

You can capture values from the URL and pass them as arguments to your view by using angle brackets in the path definition. The syntax is `<converter:name>`, where:

- `converter` specifies the type of variable (e.g., `str`, `int`, `slug`, `uuid`, `path`).
- `name` is the variable name passed to the view.

On `urls.py`:

```python
from django.urls import path
from .views import book_detail

urlpatterns = [
    path('books/<int:book_id>/', book_detail, name='book_detail'),
]
```

On `views.py`:

```python
def book_detail(request, book_id):
    # book_id is captured from the URL
    ...
```

In this example, visiting `/books/5/` will call `book_detail(request, book_id=5)`.

### 6.2. View method to templates: `render()`

Django provides the `render(request, template, var_dicctionary)` shortcut from `django.shortcuts` to combine a template with a context dictionary and return an `HttpResponse` object. This is the most common way to return HTML responses from
your views.

**Basic usage:**

```python
from django.shortcuts import render


def book_list(request):
    books = [...]
    return render(request, 'book_list.html', {'books': books})
```

- `'book_list.html'` is the template file. By default search in `app/templates/`.
- `{'books': books}` is the context dictionary, making the `books` variable available in the template.

> Using `render()` is preferred over manually creating `HttpResponse` objects with HTML, as it keeps your code clean and maintainable.

## 7. Templates

In Django, **templates** help separate the presentation layer (HTML) from the business logic handled in your views. Templates allow you to dynamically generate HTML pages by embedding variables and control structures—such as loops and conditionals—directly into your HTML files.

- Keeps your code organized by separating logic (views) from presentation (templates).
- Makes it easier to update the look and feel of your site without changing Python code.
- Supports reusability with template inheritance and includes.

### 7.1. Basic strucutre for HTML templates

Templates can contain:

- HTML tags:
    - In `<head>`:  `<meta charset="UTF-8">`, `<title>`
    - In `<body>`:  `<div> <p> <ul> <li> <table>...`
- `{{ variable_name }}` - for displaying data.
- `{% tag %}` - for control flow (e.g., loops, conditions, includes). *Sentence such as loops need an end staments.*

```html
<!DOCTYPE html>
<html>
  <head>
      <meta charset="UTF-8">
      <title>Books page</title>
  </head>
  <body>
    <h1> Book page title </h1>
    <ul>
        {% for book in books %}
        <li>
            {{ book.title }} by {{ book.author }}
        </li>
        {% endfor %}
    </ul>
  </body>
</html>
```

## 8. Using Model Classes in Views and Templates

Django models provide a powerful way to interact with your database directly from your views and templates. By leveraging model classes, you can easily query, display, and manipulate data in your application.

### 8.1. Accessing Model Data in Views

To use a model in your view, import it and use the model manager (`objects`) to perform database operations. Common operations include retrieving all records, filtering, ordering, and counting.

- `Model.objects.all()`: Returns all records as a QuerySet.
- `Model.objects.filter(...)`: Returns records matching specific criteria.
- `Model.objects.get(...)`: Returns a single record matching criteria (raises error if not found or multiple results).
- `Model.objects.order_by('field')`: Orders records by the specified field. Use `-field` for descending order.
- `Model.objects.count()`: Returns the number of records.

> For safer single-object retrieval, use `get_object_or_404(Model, pk=id)` from `django.shortcuts` to return a 404 error if the object does not exist.

### 8.2. Using Model Data in Templates

Pass the queried data to your template via the context dictionary. In the template, use Django’s template language to loop through and display the data.

**Exampe**

```html
<h1>Book List</h1>
<p>Number of books: {{ total_books }}</p>
<ul>
    {% for book in books %}
        <li>{{ book.title }} by {{ book.author }}</li>
    {% empty %}
        <li>No books available.</li>
    {% endfor %}
</ul>
```

- Use `{{ variable }}` to display variables passed from the view.
- Use `{% for ... %}` to iterate over QuerySets.
- `{% empty %}` provides a fallback if the list is empty.

### 8.3. Detail View Example

0. You can create links to detail pages for each object using their primary key or another unique identifier.

**Example:**

```html
<ul>
    {% for book in books %}
        <li>
            {{ book.title }} by {{ book.author }}
            <a href="{% url 'book_detail' book.id %}">Details</a>
        </li>
    {% endfor %}
</ul>
```

1. Make sure to define the corresponding URL pattern in your `urls.py`:

```python
from django.urls import path
from .views import book_detail

urlpatterns = [
    path('books/<int:id>/', book_detail, name='book_detail'),
]
```


> Can use a model from other app includin it `from app_x.models import model_class_x` on views file.

2. Define the view function

```python
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, 'book_detail.html', {'book': book})
```

3. Create the template 
   

```html
...
<h2>{{ book.title }}</h2>
<p>Author: {{ book.author }}</p>
<p>Published: {{ book.published_date }}</p>
<p>Description: {{ book.description }}</p>
...
```

By using model classes in your views and templates, you can efficiently display and manage data throughout your Django application: `book_list.html`.

## 9. Using ModelForm Class in Views and Templates

> If you do not implemente a ModelForm can use `mdoelform_factory(ModelClassName, exclude= [])` from `django.form` module. *`exclude` indicete params which do not use on the from.*

Django’s **ModelForm** simplifies the process of creating forms tied to your models, making it easy to add, edit, and delete database records through user-friendly HTML forms.

- **Automatic form generation:** Fields are created based on your model, reducing repetitive code.
- **Validation:** Built-in validation ensures submitted data matches your model’s requirements.
- **Synchronization:** Changes to your model are reflected in the form automatically.
- **Easy saving:** Validated form data can be saved directly to the database.


### 9.1. Interaccion with database

When using a ModelForm in Django, interaction with the database is streamlined and handled through the form’s methods. Here’s how the process works:

- **Creating (Adding) Objects:**  
    When you call `form.save()` after validating the form (`form.is_valid()`), Django creates a new instance of the model and saves it to the database.

- **Updating Objects:**  
    If you pass an existing model instance to the form (using the `instance` parameter), `form.save()` will update that object in the database with the new data from the form.

- **Deleting Objects:**  
    To delete an object, retrieve it (usually with `get_object_or_404`), then call its `.delete()` method. This removes the record from the database.


> - Always check `form.is_valid()` before calling `save()` to ensure data integrity.
> - The `save()` method can take `commit=False` if you want to modify the instance before saving to the database.

For more details, see the [official Django ModelForm documentation](https://docs.djangoproject.com/en/stable/topics/forms/modelforms/).


### 9.2. CSRF Protection in Django Forms

Django includes built-in protection against Cross-Site Request Forgery (CSRF) attacks for all POST forms. CSRF is a security vulnerability where unauthorized commands are transmitted from a user that the web application trusts.

To enable CSRF protection in your forms, always include the `{% csrf_token %}` template tag inside every `<form>` that uses the POST method. This tag generates a hidden input field with a unique token for each session, which Django checks on form submission.

**Example:**

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
```

If you omit `{% csrf_token %}`, Django will reject POST requests with a "403 Forbidden" error.

For more details, see the [official Django CSRF documentation](https://docs.djangoproject.com/en/stable/ref/csrf/).

### 9.3. Basic Workflow

1. **Define a ModelForm** in your app’s `forms.py`:

    ```python
    from django import forms
    from .models import Book

    class BookForm(forms.ModelForm):
        class Meta:
            model = Book
            fields = '__all__'  # or specify a list of fields
    ```

2. **Use the form in your view** to handle GET and POST requests:

    ```python
    from django.shortcuts import render, redirect

    def add_book(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        else:
            form = BookForm()
        return render(request, 'add_book.html', {'form': form})
    ```
> Don't forget to include in `ulrs.py`the path.
3. **Render the form in your template**:

    ```html
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>
    ```

### 9.4. Editing and Deleting Objects

- **Edit:** Pass the instance to the form to pre-fill data and update the object.

    ```python
    def edit_book(request, id):
        book = get_object_or_404(Book, pk=id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        else:
            form = BookForm(instance=book)
        return render(request, 'edit_book.html', {'form': form})
    ```

- **Delete:** Retrieve the object and call `.delete()`, then redirect.

    ```python
    def delete_book(request, id):
        book = get_object_or_404(Book, pk=id)
        book.delete()
        return redirect('book_list')
    ```