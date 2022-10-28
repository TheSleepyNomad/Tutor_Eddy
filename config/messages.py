from enum import Enum

# start message templates
start_msg = """
Привет, дорогой гость! Меня зовут Тутор Эдди =)
И как ты мог заметить - я бот!

Позволь начать наше знакомство с меня)
Сейчас ты мой гость! Поэтому я могу:
 - помочь записаться на пробное занятие
Я помогу тебе связаться с Марией, а так же расскажу
подробнее о занятиях и ценах. А если тебе понравится
Мария как репетитор, то я помогу тебе узнать когда у тебя
следующий урок

Для первоначальной настройки тебе всего лишь надо
выбрать язык на которым ты хочешь общаться и поделиться 
своим телефоном
"""
choose_language_msg = """
Давай начнем с языка?
Продолжим на русском или же
you prefer English?
"""
set_user_settings = """
Отлично! Последний шаг это твой телефон. Он нужен для того,
чтобы Мария могла связаться с тобой, а также восстановить
с тобой связь, если будут проблемы с контактами. Бэкапы ведь
всегжа нужны)
"""
guests_start_msg = "С возвращением в главное меню, {}"
students_start_msg = "Чем я могу помочь, {}?"
admin_start_msg = """
Привет, {}! Сегодня у тебя {} занятий. А также
{} хочет записаться на занятие =) Начнем работу?
"""

# about message templates
about_tutor_msg = 'О Марии...'
about_app_msg = 'О Программе...'
about_lessons_msg = 'Подробнее о предметах'
about_lesson_msg = """
Ученик: {}
Телефон: {}
Предмет: {}
Дата: {}
Занятие оплачено: {} 
"""
about_math_msg = 'Подробнее о математике'
about_eng_msg = 'Подробнее о английском'
about_social_msg = 'Подробнее о обществознании'

# help message templates
help_msg = 'Помощь по работе в программе'


class MsgTemplates(str, Enum):
    """
    Stores message templates for users
    """
    START_MSG = start_msg
    CHOOSE_LANG_MSG = choose_language_msg
    SET_USR_SETTING = set_user_settings
    GUEST_START_MSG = guests_start_msg
    STUDENTS_START_MSG = students_start_msg
    ADMIN_START_MSG = admin_start_msg
    ABOUT_TUTOR_MSG = about_tutor_msg
    ABOUT_APP_MSG = about_app_msg
    ABOUT_LESSONS_MSG = about_lessons_msg
    ABOUT_LESSON_MSG = about_lesson_msg
    ABOUT_MATH_MSG = about_math_msg
    ABOUT_ENG_MSG = about_eng_msg
    ABOUT_SOCIAL_MSG = about_social_msg
    HELP_MSG = help_msg
