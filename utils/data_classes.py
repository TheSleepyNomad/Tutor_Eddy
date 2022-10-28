from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class LessonRecord:
    lesson_id: int
    student_id: int
    lesson_type_id: int
    student_name: str
    student_phone: str
    lesson_name: str
    lesson_date: datetime or str
    is_payment: bool
    is_test_lesson: bool
