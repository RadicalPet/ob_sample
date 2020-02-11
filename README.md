# ob_sample

## Setup

- pip install requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py getfeed


### API URLS

Log in with superuser credentials from previous step.

* http://localhost:8000/api/languages
** lists languages from all Shopify (the organization) repos

* http://localhost:8000/api/comments
** lists all commit comments on the 3 Shopify sample repos

* http://localhost:8000/api/repos?limit=50
** lists the 50 recent-most created repos of the Shopify organization
