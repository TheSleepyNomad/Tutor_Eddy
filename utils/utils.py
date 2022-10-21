from typing import List, Tuple
from config.settings import ADMIN_NAME
from utils.data_classes import LessonRecord
from datetime import datetime


def check_admin_role(username: str) -> bool:
    return True if username == ADMIN_NAME else False


def _convert_in_class(query_result: List[str]) -> List[LessonRecord]:
    recors_list = []
    print(query_result)
    for item in query_result:
        recors_list.append(
            LessonRecord(
                lesson_id=item[0],
                student_id=item[1],
                lesson_type_id=item[2],
                student_name= f'{item[7]} {item[8]}',
                student_phone=item[9],
                lesson_name=item[6],
                lesson_date= item[3] if item[3] else 'Пробное занятие',
                is_payment=item[4],
                is_test_lesson=item[5],
            )
        )
    
    return recors_list