from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from schema import create_class
from models import modedel_base_section_db

# ap2


def get_all(db: Session):
    return db.query(modedel_base_section_db).all()


# api2
def shearch_team_sv(subject_name: str, db: Session):
    return (db.query(modedel_base_section_db).filter(modedel_base_section_db.subject_name.like(f"%{subject_name}%")).all())


# api 3


def get_by_id(section_id: int, db: Session):
    team = (
        db.query(modedel_base_section_db).filter(modedel_base_section_db.id == section_id).first())
    if team is None:
        raise HTTPException(tatus_code=status.HTTP_404_NOT_FOUND, detail="không tìm thấy lớp")
    return team


#  api 4


def post_class(new_class: create_class, db: Session):
    team = modedel_base_section_db(**new_class.model_dump())
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


# api 5


def put_class(section_id: int, update: create_class, db: Session):
    team = (
        db.query(modedel_base_section_db)
        .filter(modedel_base_section_db.id == section_id)
        .first()
    )
    if team is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="khong tim thay lop")
    team.subject_name = update.subject_name
    team.class_code = update.class_code
    team.teacher_name = update.teacher_name
    team.student_count = update.student_count
    db.commit()
    db.refresh(team)
    return team


# api 6

def delete_class(section_id: int, db: Session):
    team = (db.query(modedel_base_section_db).filter(modedel_base_section_db.id == section_id).first())
    if team is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy lớp học phần")
    db.delete(team)
    db.commit()
