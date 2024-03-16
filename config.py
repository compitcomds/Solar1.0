import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'this_is_test_SECRET_KEY')
    # DEBUG = os.getenv('DEBUG', '').lower() == 'true'
    MONGO_URI = os.getenv('MONGO_URI')
    CACHE_TYPE = os.getenv('CACHE_TYPE')
    CACHE_DEFAULT_TIMEOUT = int(os.getenv('CACHE_DEFAULT_TIMEOUT', 300))
    MAIL_KEY = os.getenv('MAIL_KEY')
    Azure_blob_service_client = os.getenv('Azure_blob_service_client')
    AZURE_STORAGE_CONNECTION_STRINGS = os.getenv('AZURE_STORAGE_CONNECTION_STRING')