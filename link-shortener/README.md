# link-shortener

An application for keeping shortened links.

### Usage:
1. Clone this repository.
2. Change the directory to the cloned folder.
3. Run `pipenv shell` in the command line.
4. Run `flask run` in the command line.
5. Open `localhost:5000` in the browser.

### Technologies:
- Flask
- Python
- SQLite
- Pipenv

### Pages:
- `localhost:5000`.
- `localhost:5000/stats`.
- `localhost:5000/add_link`.

### Create Database (CMD):
- `python`.
- `from link_shortener import create_app`.
- `from link_shortener.extensions import db`.
- `from link_shortener.models import Link`.
- `db.create_all(app=create_app())`.

### View Database:
- Run `sqlite3 link_shortener/db.sqlite3` in the command line to view the database.
- Run `.tables` in the shell (SQLite) to see the list of tables.
- Run `select * from link;` in the shell (SQLite) to see all the links.
- Run `.schema link` in the shell (SQLite) to view the table structure.
- Run `.exit` in the shell (SQLite) to exit the shell.
- Make sure that your queries have semicolons.

### Authentication:
- The username is `admin`.
- The password is `password`.

### Complete:
1. Button for copying links.
2. Change background color.
3. Navigation bar for routes.
4. Input is required.
5. Add delete functionality.
6. Add update functionality.
7. Make sure the link is valid.
