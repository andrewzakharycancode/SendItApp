# SendItApp

## How to run SendIt Django
1. Start your Virtual Environment
     
    - Windows
   ```
   .venv\Scripts\Activate.ps1
   ```
    - Linux
   ```
   source .venv/bin/activate
   ```
   #### How to create a virtual environment called .venv, if the above doesn't work:
   - Windows
   ```
    python -m venv .venv
   ```
    - Linux
   ```
    python3 -m venv .venv
   ```
2. Run the Django Server
    - Windows
   ```
    python manage.py runserver
   ```
    - Linux
   ```
    python3 manage.py runserver
3. Navigate to http://127.0.0.1:8000/

## How to run database migrations / create database tables from Django Models
1. Make any necessary changes to models.py (new tables, new columns, new relationships, data type changes, etc)
2. Run the following:
   ```
   python manage.py makemigrations SendItDjango
   ```
   ```
   python manage.py migrate SendItDgango
   ```
3. Check your changes were made via command line:
   1. Connect to Postgres
   ```
   psql -h senditapp-database.cjuh9o86togv.us-east-2.rds.amazonaws.com -U postgres -d postgres -p 5432
   ```
   2. Run a SQL command to check your changes, e.g.
   ```
   SELECT * FROM table WHERE id=1
   ```
## How to run SendIt React
From the SendItReact directory:
1. `npm start`
2. `npm run ios` -> for running iOS simulator
3. `npm run android` -> for running Android simulator