# ob_sample

## Setup

- `pip install -r requirements.txt`
- export a github auth token to the environment (`export AUTH_TOKEN=xxxxxxxxxxx`)
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py getfeed`
- `python manage.py runserver`


### API URLS

Log in with superuser credentials from previous step.

* http://localhost:8000/api/languages
  * lists languages from all Shopify (the organization) repos

* http://localhost:8000/api/comments
  * lists all commit comments on the 3 Shopify sample repos

* http://localhost:8000/api/repos?limit=50
  * lists the 50 recent-most created repos of the Shopify organization
