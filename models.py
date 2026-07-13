from database import Base ,engine
from sqlalchemy import Column , String ,Integer

class modedel_base_section_db(Base) :
    __tablename__ = 'class_sections'
    id = Column(Integer , primary_key=True , autoincrement=True)
    subject_name = Column(String(200))
    class_code = Column(String(200)) 
    teacher_name = Column(String(200)) 
    student_count = Column(Integer)

Base.metadata.create_all(bind=engine)