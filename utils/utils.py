from typing import List, Tuple
from config.settings import ADMIN_NAME
from utils.data_classes import LessonRecord
from datetime import datetime


def check_admin_role(username: str) -> bool:
    return True if username == ADMIN_NAME else False


def _convert_in_class(query_result: List[str]) -> List[LessonRecord]:
    recors_list = []
    for item in query_result:
        recors_list.append(
            LessonRecord(
                student_id=item[0],
                lesson_type_id=item[1],
                student_name= f'{item[6]} {item[7]}',
                student_phone=item[8],
                lesson_name=item[5],
                lesson_date= item[2] if item[2] else 'Пробное занятие',
                is_payment=item[3],
                is_test_lesson=item[4],
            )
        )
    
    return recors_list