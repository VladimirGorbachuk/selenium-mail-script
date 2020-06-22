import os
from os.path import join, dirname
from dotenv import load_dotenv

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

GMAIL_USERNAME=os.environ['GMAIL_USERNAME']
GMAIL_PASSWORD=os.environ['GMAIL_PASSWORD']
EXECUTOR_HUB=os.environ['EXECUTOR']
EMAIL_AUTHOR_TO_FIND=os.environ['EMAIL_AUTHOR_TO_FIND']
