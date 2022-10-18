from os import getenv, path
from dotenv import load_dotenv
from emoji import emojize


load_dotenv()

# telegram bot token
TOKEN = getenv('BOT_TOKEN')

# project root
BASE_DIR = path.dirname(path.abspath(__file__))

# db settings
DB_NAME = 'journal.db'
DATABASE = path.join('sqlite:///' + BASE_DIR, DB_NAME)

# for utils and other
ADMIN_NAME = getenv('ADMIN_NAME')

# control btns
KEYBOARD = {
    # for admin
    'LESSONS': emojize(':book: Все записи'),
    'ADD_STUDENT': emojize(':busts_in_silhouette: Новый ученик'),
    # for students
    'MY_LESSONS': emojize(':books: Мои занятия'),
    'APP_INFO': emojize(':speech_balloon: О программе'),
    'REQ_PHONE': emojize(':open_file_folder: Поделиться телефоном'),
    # for guest
    'INFO': emojize(':speech_balloon: О Марии...'),
    'TEST_LESSON': emojize(':pencil: Пробное занятие'),
    # other
    '<<': emojize('⏪'),
    'SETTINGS': emojize('⚙️ Настройки'),
}
