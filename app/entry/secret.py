import os

DATABAE_NAME = os.environ.get("DATABAE_NAME")  # <DATABAE_NAME>
DATABAE_USERNAME = os.environ.get("DATABAE_USERNAME")      # <DATABAE_USERNAME>
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")  # <DATABASE_PASSWORD>
# SECURITY WARNING: keep the secret key used in production secret!
MY_SECRET_KEY = os.environ.get("MY_SECRET_KEY") 
