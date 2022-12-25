# Weather-Application
This repository implements a weather app that uses Open Weather API and Django as a backend framework.

Project is created with- Djano, OpenWeatherMap

## Summary Workflow
The following is a basic workflow that you can use as a quick reference for developing a Django Project.

### Setup
 on cmd ---
1. mkdir authsystem
2. cd authsystem
3. py -m venv venv
4. venv\Scripts\activate.bat
5. pip install django
6. Collecting django
7. pip install django_crispy_forms
8. django-admin
9. django-admin startproject authsysproject

### Add Basic URLs and Views
1. Map your Project’s urls.py file to the new app.
2. In your App directory, create a urls.py file to define your App’s URLs.
3. Add views, associated with the URLs, in your App’s views.py; make sure they return a HttpResponse object. Depending on the situation, you may also need to query the model (database) to get the required data back requested by the end user.

### Templates and Static Files
1. Create a templates and static directory within your project root.
2. Update settings.py to include the paths to your templates.
3. Add a template (HTML file) to the templates directory. Within that file, you can include the static file with - <pre>{% load static %}</pre> and <pre> {% static "filename" %} </pre>. Also, you may need to pass in data requested by the user.
4. Update the views.py file as necessary.

### Models and Databases
1. Update the database engine to settings.py (if necessary, as it defaults to SQLite).
2. Create and apply a new migration.
3. Create a super user.
4. Add an admin.py file in each App that you want access to in the Admin.
5. Create your models for each App.
6. Create and apply a new migration. (Do this whenever you make any change to a model).

### Forms
1. Create a forms.py file at the App to define form-related classes; define your ModelForm classes here.
2. Add or update a view for handling the form logic - e.g., displaying the form, saving the form data, alerting the user about validation errors, etc.
3. Add or update a template to display the form.
4. Add a urlpattern in the App’s urls.py file for the new view.

### User Registration
1. Create a UserForm
2. Add a view for creating a new user.
3. Add a template to display the form.
4. Add a urlpattern for the new view.

### User Login
1. Add a view for handling user credentials.
2. Create a template to display a login form.
3. Add a urlpattern for the new view.

### Setup the template structure
1. Find the common parts of each page (i.e., header, sidebar, footer).
2. Add these parts to a base template
3. Create specific. templates that inherent from the base template.

# Working Project

https://user-images.githubusercontent.com/78306516/209458016-774c10d0-07ac-4f95-97e1-dbd960b0d7e4.mp4

