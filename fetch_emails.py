# fetch_emails.py

import os.path
import pickle
import logging

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

from config import CLIENT_SECRET_FILE, GMAIL_SCOPES, TOKEN_FILE
from models import store_email, Email

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def authenticate_gmail():
    """
    Authenticates the user using OAuth2 and returns the Gmail API service object.

    Returns:
        service: The authenticated Gmail API service object.
    """
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, GMAIL_SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

def fetch_emails(service):
    """
    Fetches emails from the user's Gmail inbox.

    Args:
        service: The authenticated Gmail API service object.

    Returns:
        list: A list of messages from the inbox.
    """
    try:
        results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = results.get('messages', [])
        return messages
    except Exception as e:
        logger.error(f"Error fetching emails: {e}")
        return []

def main():
    service = authenticate_gmail()
    emails = fetch_emails(service)
    for email in emails:
        # Process each email and store it in the database
        store_email(email)  # Add your email processing and storage logic here

if __name__ == "__main__":
    main()

