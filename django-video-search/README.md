# django-video-search

An application for searching YouTube.

### Usage:
- `git clone https://github.com/jacobc2700/django-video-search.git`.
- `cd django_video_search`.
- `pipenv shell`.
- `pipenv install`.
- `cd django_video_search`.
- `python manage.py runserver`.
- `localhost:8000`.

### API:
- Get a key for the `YouTube Data API v3` from the `Google API Library Console`.
- Go to the `django_video_search/django_video_search/settings.py` file and put your key at the bottom.

### Info:
- Starting the application:
- `django-admin startproject django_video_search`.
- `cd django_video_search`.
- `python manage.py startapp search`.
- Main files:
- `django_video_search/search/views.py`.
- `django_video_search/search/templates/search/index.html`.

### Technologies:
- Django
- Python
- YouTube
- Google API
- Pipenv