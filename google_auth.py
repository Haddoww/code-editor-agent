# google_auth.py
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# Google Docs requires this scope
SCOPES = ['https://www.googleapis.com/auth/documents', "https://www.googleapis.com/auth/drive"]

def get_docs_service():
    creds = None
    token_path = 'token.json'

    # Load existing token if available
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # If no valid creds, run the auth flow
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=8888)
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

    return build('docs', 'v1', credentials=creds)
