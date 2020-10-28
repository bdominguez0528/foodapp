# Django App Bootstrap

[![](https://github.com/swappsco/django-app-bootstrap/workflows/py.test/badge.svg)](https://github.com/swappsco/sidoc/workflows/py.test/badge.svg)
[![](https://cdn.swapps.com/uploads/2020/07/coverage100.png)](https://cdn.swapps.com/uploads/2020/07/coverage100.png)

**Requirements:**

- Python 3.6+

Django version: 3.0

## Project Setup

### Unix Linux systems

You need to have a database called sidoc without password in your local instance, otherwise you will have to create a .env with DATABASE_URL variable defined.

```plain
# Install JS requirements
yarn
# Run watcher for assets compilation
yarn run watch

pip install -r requirements/local.txt
python manage.py migrate
python manage.py runserver
```

## Windows

Requirements:

- [Vagrant](https://www.vagrantup.com/downloads)
- [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [NodeJS](https://nodejs.org/en/download/)

Clone the repository and run inside the cloned folder this:

```plain
npm -g install yarn
yarn
yarn run build
vagrant up
```

It will create a virtual machine and will run the projects on [http://localhost:8000](http://localhost:8000)

## Testing Checks

These checks are required to pass to accept code in the repository

```plain
# Unit Testing
pytest

# Static validation
mypy .

# linting validation
black --check .
```

# Development considerations

Webpack was configured to have 2 different main sources depending on the required layout: Dashboard pages and Login pages.

## Base files

Base template:

`app/templates/base.html`

JS main file:

`app/static/js/index_app_.js`

SASS main file:

`app/static/sass/index_app_.scss`
