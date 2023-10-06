from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api.hsk.repository.question.model import QuestionEntity, QuestionModel, QuestionUpdateModel


def get_question(id: int, db: Session):
    return db.query(QuestionEntity).filter(QuestionEntity.id == id).first()


def create_question(question: QuestionModel, db: Session):
    new_question = QuestionEntity(**question)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question


def update_question(id: int, question: QuestionUpdateModel, db: Session):
    db_item = db.query(QuestionEntity).filter(
        QuestionEntity.id == int(id)).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.general = question["general"]
    db_item.content = question["content"]
    db.commit()
    db.refresh(db_item)
    return db_item
