# django-weather

An application for viewing the weather in the world.

### Usage:
1. Clone this repository.
2. Change the directory to the cloned folder.
3. Run `virtualenv venv` in the command line.
4. Run `venv\Scripts\activate` in the command line.
5. Run `pip install -r requirements.txt` in the command line.
6. Open the `django_weather/weather/views.py` file and add your `OpenWeatherMap API Key` in the form of `http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={API_KEY}`.
7. Run `python manage.py runserver` in the command line.
8. Open `localhost:8000` in the browser.

### Administrator:
- Open `localhost:8000/admin` in the browser.
- Log in with the credentials you specified for your super user account.

### Manage Cities:
- Admin dashboard.
- User interface.
- Shell commands.

### Project Creation:
- `mkdir django_weather`.
- `django-admin startproject django_weather`.
- `cd django_weather`.
- `python manage.py startapp weather`.
- `python manage.py migrate`.
- `python manage.py createsuperuser`.
- `python manage.py runserver`.
- `localhost:8000`.

### Migrations:
- `python manage.py makemigrations`.
- `python manage.py migrate`.

### Database (SQLite):
- `cd django_weather`.
- `sqlite3 db.sqlite3`.
- `.tables`.
- `select * from weather_city;`.
- `.exit`.

### Technologies:
- Django
- Python
- Pipenv
- Weather API