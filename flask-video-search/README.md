# flask-video-search

An application for searching YouTube.

### Usage:
1. Clone this repository.
2. Change the directory to the cloned folder.
3. Run `pipenv shell` in the command line.
4. Run `pipenv install` in the command line.
5. Get the `YouTube Data API v3` key from the `Google Console API Library`.
6. Put the key that you get in the `.env` file.
7. Run `flask run` in the command line.
8. Open `localhost:5000` in the browser.

### Debug:
- There is a problem with debug mode.
- Everytime I try to add `FLASK_ENV=development` to the `.flaskenv` file, the application will not run.