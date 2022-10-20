from enum import Enum

# start message templates
start_msg = "Стартовое сообщение"
choose_language_msg = 'какой язык использовать?'
guests_start_msg = "Стартовое сообщение для гостя"
students_start_msg = "Стартовое сообщение для студентов"
admin_start_msg = 'Стартовое сообщение для админа'

# about message templates
about_tutor_msg = 'О Марии...'
about_app_msg = 'О Программе...'
about_lessons_msg = 'Подробнее о предметах'
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
    GUEST_START_MSG = guests_start_msg
    STUDENTS_START_MSG = students_start_msg
    ADMIN_START_MSG = admin_start_msg
    ABOUT_TUTOR_MSG = about_tutor_msg
    ABOUT_APP_MSG = about_app_msg
    ABOUT_LESSONS_MSG = about_lessons_msg
    ABOUT_MATH_MSG = about_math_msg
    ABOUT_ENG_MSG = about_eng_msg
    ABOUT_SOCIAL_MSG = about_social_msg
    HELP_MSG = help_msg
