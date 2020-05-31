# flask-weather

An application for viewing the weather in the world.

### Usage:
1. Clone this repository.
2. Change the directory to the cloned folder.
3. Run `pipenv shell` in the command line.
4. Run `pipenv install` in the command line.
5. Get an API key from OpenWeatherMap.
6. Put the key in the `app.py` file like this: `http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}`.
7. Create the database by following the section below.
8. Run `flask run` in the command line.
9. Open `localhost:5000` in the browser.

### Database:
- `python`.
- `from app import db`.
- `db.create_all()`.
- `sqlite3 weather.db`.
- `select * from city;`.
