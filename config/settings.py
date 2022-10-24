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
    'LESSONS': '\U0001F4D6'+'Записи',
    'ALL_LESSONS': 'Все Записи',
    'ADD_LESSON': 'Новая запись',
    'CHANGE_LESSON': 'Изменить запись',
    'STUDENTS': emojize(':busts_in_silhouette: Ученики'),
    'MY_STUDENTS': 'Мои ученики',
    'MY_GUESTS': 'Новые ученики',
    # for students
    'MY_LESSONS': emojize(':books:Мои занятия'),
    'REQ_PHONE': '\U0001F4F2' + 'Поделиться телефоном',
    # for guest
    'ABOUT_TUTOR': '\U0001F469\U0000200D\U0001F3EB' + 'О Марии...',
    'TEST_LESSON': '\U0001F4C5' + 'Пробное занятие',
    # other
    'HELP': emojize(':speech_balloon:Помощь'),
    '<<': emojize('⏪ Назад'),
    'SETTINGS': emojize('⚙️Настройки'),
    'ABOUT_APP': emojize(':red_question_mark:О программе'),
    'MATH': emojize(':triangular_ruler:Математика'),
    'ENGLISH': emojize(':european_castle:Английский язык'),
    'SOCIAL': emojize(':hammer:Обществознание'),
    'RUS': '\U0001F1F7\U0001F1FA' + 'Русский',
    'ENG': '\U0001F1EC\U0001F1E7' + 'English',
    'LANGUAGE': emojize(':gb:Язык'),
    'CHANGE_LNG': '\U0001F30D' + 'Сменить язык',
}
