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
ADMIN_ID = getenv('ADMIN_ID')

# control btns
KEYBOARD = {
    # for admin
    'LESSONS': emojize(':book: Журнал уроков'),
    'ADD_STUDENT': emojize(':busts_in_silhouette: Ученики'),
    # for students
    'MY_LESSONS': emojize(':books:Мои занятия'),
    'REQ_PHONE': emojize(':iphone:Поделиться телефоном'),
    # for guest
    'ABOUT_TUTOR': emojize(':information_desk_person:О Марии...'),
    'TEST_LESSON': emojize(':date:Пробное занятие'),
    # other
    'HELP': emojize(':speech_balloon:Помощь'),
    '<<': emojize('⏪ Назад'),
    'SETTINGS': emojize('⚙️Настройки'),
    'ABOUT_APP': emojize(':red_question_mark:О программе'),
    'MATH': emojize(':triangular_ruler:Математика'),
    'ENGLISH': emojize(':european_castle:Английский язык'),
    'SOCIAL': emojize(':hammer:Обществознание'),
    'RUS': emojize(':ru:Русский'),
    'ENG': emojize(':gb:English'),
    'LANGUAGE': emojize(':gb:Язык'),
    'CHANGE_LNG': emojize(':gb:Сменить язык'),
}
