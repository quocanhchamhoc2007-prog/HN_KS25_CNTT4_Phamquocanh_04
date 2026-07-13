from pydantic import BaseModel

class create_class(BaseModel) :
    subject_name :str
    class_code :str 
    teacher_name :str
    student_count :int