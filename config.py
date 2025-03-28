import os
import socket
from dotenv import load_dotenv
 
# Load from .env file (defaults to looking for ".env" in the current directory)
load_dotenv()

def is_production():
    """Check if we're running on the production server by hostname"""
    return os.getenv("PROD_HOSTNAME") in socket.gethostname()
 
# Set base path depending on environment
BASE_PATH = '/100DoC/day2-tip' if is_production() else ''
STATIC_PATH = f'{BASE_PATH}/static'
 
# For debugging
if __name__ == '__main__':
    print(f"Running in {'production' if is_production() else 'development'} mode")
    print(f"BASE_PATH: {BASE_PATH}")
    print(f"STATIC_PATH: {STATIC_PATH}") 