# Pass.NET
### *__Pass__.__NET__* is a service which can generate and save to db: logins, random passwords, pin-codes, secret keys for git or django, hash keys and much more.
1. Firstly, you need to add venv file by this command:
   ```
   python -m venv venv
2. Update pip:
   ```
   pip install --upgrade pip
3. Install dependencies from requirements:
   ```
   pip install -r requirements.txt 
4. Create a ".env" file at the root of the directory with params:
   ```python
   ALL SETTINGS FOR POSTGRESQL
   
   DB_USER=your postgres user
   DB_PASS=your password for user
   DB_NAME=your name of db
   DB_HOST=127.0.0.1 or localhost
   DB_PORT=5432
   

   SMTP_USER=your email address 
   SMTP_PASS=search the Internet how to get it
5. Before starting the project you must do alembic's migration:
   ```
   alembic upgrade head
6. After that start the project(in main.py or by a command), celery and flower:  
    ```python
    1) uvicorn src.main:app --reload
    2) celery -A src.tasks.tasks:celery worker --loglevel=INFO
    3) celery -A src.tasks.tasks:celery flower
