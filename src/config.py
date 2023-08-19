from dotenv import load_dotenv
import os

load_dotenv()


DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

DB_TEST_HOST = os.environ.get('DB_TEST_HOST')
DB_TEST_PORT = os.environ.get('DB_TEST_PORT')
DB_TEST_NAME = os.environ.get('DB_TEST_NAME')
DB_TEST_USER = os.environ.get('DB_TEST_USER')
DB_TEST_PASS = os.environ.get('DB_TEST_PASS')

SMTP_PASS = os.environ.get('SMTP_PASS')
SMTP_USER = os.environ.get('SMTP_USER')
