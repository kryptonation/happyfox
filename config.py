# config.py

import os

GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
CLIENT_SECRET_FILE = 'credentials.json'  # Path to your credentials.json file
TOKEN_FILE = 'token.pickle'  # Path to your token.pickle file
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///processed_emails.db')