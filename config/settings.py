from os import getenv, path
from dotenv import load_dotenv

load_dotenv()

# telegram bot token
TOKEN = getenv('BOT_TOKEN')

# project root
BASE_DIR = path.dirname(path.abspath(__file__))

# db settings
DB_NAME = 'journal.sqlite'
DATABASE = path.join('sqlite:///' + BASE_DIR, DB_NAME)
