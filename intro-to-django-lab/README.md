# Lab: Django Basics lab


## 0- Setup
1. Use the document Omar provided [here](https://docs.google.com/document/d/1RBjpbDs7AX9sDOom-xrHYfx66TA1VzJ11jhU4EsC7dU/edit?usp=sharing) to set up your virtual environment and django application.
2. In the document set up until step 13
3. If you do the setup here using the document you can skip the lab steps up to step 6 directly in this lab

## 1- Create the project folder & virtual environment

1. Create a new folder for the lab and enter it.
2. Create a **virtual environment** in that folder.
3. **Activate** the virtual environment.
4. Confirm the Python shown in your terminal comes from the venv.



---

## 2- Install dependencies

1. Install **Django**.
2. Install **psycopg2-binary**


---

## 3- Start the Django project & app

2. Create a new app named `first_lab_app`.
3. Explore the created files so you understand what each does.

---

## 4- Register the app in settings

1. Open `settings.py`.
2. Add the `first_lab_app` app to `INSTALLED_APPS`.


---


## 5- Configure PostgreSQL as the database

1. In `settings.py`, replace the default DB with a **PostgreSQL** configuration.
2. Use your real credentials: DB name, user, password, host, port.


---




## 6- Create a base.html
1. Create a base.html that has 2 blocks: head block and a content block
2. Load the static files in this file


## 7- Create 2 views
1. homepage view
2. about view

## 8- Create the templates for the views
1. In your templates folder create the html pages for the views

## 9- wire up the routes in the urls.py
1. Create two urls for both pages
2. in the about display all the technologies you worked with in this class
3. give a class name of python or javascript for python or javascript specific technologies
4. in a css file make the javascript technologies yellow and python blue
5. BONUS: create the technologies as a dictionary in the view and pass it in the context

