# Django Test

A test project with Django. Include authentication flow, custom user, extra profile and social authentication via Facebook.

## Features

* For Django 2.1 and Python 3.7
* Custom user model
* Extra information in Profile User.
* Email/password for log in/sign up instead of Django's default username.
* Facebook authentication.

### Installation

1. Make sure Python3 is already installed.

2. Clone the repo and configure the virtual environment:

``` 
$ python3 -m venv path/to/virtualenv
$ source path/to/vitualenv/bin/activate
$ git clone https://github.com/lauraelyo/testcambas.git
$ cd testcambas
$ pip install -r requirements.txt
```

3. Set up migrations for custom user models and build the database.

```
(venv) $ python manage.py makemigrations users
(venv) $ python manage.py migrate
```

4. Create a superuser:
```
(venv) $ python manage.py createsuperuser
```

5. Run server:
```
(venv) $ python manage.py runserver
```
