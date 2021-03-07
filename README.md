# django-portfolio-public
A web portfolio made with Python and its web development Django framework. Use it as template or inspiration if you want, just give the credit.

# Acknowledge
This portfolio project has been made thanks to the [Django backend framework](https://www.djangoproject.com/) and the [Terminal CSS frontend framework](https://terminalcss.xyz/). 

# Warning
This repository doesn't include the Django settings.py file nor the wsgi.py file, you cannot deploy it directly. If you are new to Django, I suggest to check out the [official documentation](https://docs.djangoproject.com/en/3.1/). 

# Structure
This project is structured in two apps and an external templates folder:
* The `pages` app contains the static pages (about.html), and the static files that are common to the rest of the project.
* The `projects` app contains the list formatted page that shows my personal projects as Python developer.
* The external `templates` folder contains the base html templates `base.html` and `navbar.html`.

# Improvements
I am not a front-end developer so I didn't tried to tweak Terminal CSS into my very own preferences, but there is a lot to do with the mobile version of this website. Even though the low level of typography formatting is totally intended and the project is fully responsive in terms of screen size, it can be a anoying to read the `h1` and `h2` tags in little devices.