# flask-questions

A simple question and answer website.

### Usage:
- `git clone https://github.com/jacobc2700/flask-questions.git`.
- `cd flask-questions`.
- `pipenv shell`.
- `pipenv install`.

### Technologies:
- Flask
- Python
- SQLite

### SQLite:
- `flask create_tables`.
- `sqlite3 flask_questions/db.sqlite3`.
- `.tables`.
- `.exit`.

### Debug:
- There is a problem with debug mode.
- Everytime I try to add `FLASK_ENV=development` to the `.flaskenv` file, the application will not run.

### Functionality:
- Register as a user.
- Log in as a user.
- See list of answered questions.
- Ask a question and assign it to an expert.
- Log in as an expert.
- Go to unanswered questions as an expert.
- Answer questions assigned to you.
- Admin user can promote users to expert.
- Admin can see all users.

### User Type:
- You can make a regular user, an expert, or an admin.
- Go to `flask_questions/routes/auth.py` and edit these lines:
```
user = User(
    name=name, 
    unhashed_password=unhashed_password,
    admin=True,  
    expert=False
)
```
- Set `admin` and `expert` to false for making regular users.
- Set only `expert` to true for making experts.
- Set only `admin` to true for making admins.
