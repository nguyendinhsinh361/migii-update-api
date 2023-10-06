import json
from fastapi import HTTPException
from app.api.hsk.repository.question.model import QuestionModel, QuestionUpdateModel
from app.config.hsk.database import Base, engine
from sqlalchemy.orm import Session
from app.api.hsk.repository.question.repo import get_question, create_question, update_question
from app.api.hsk.repository.question_test.repo import update_question_test_option


def question_get(id: str, db: Session):
    question = get_question(db, id)
    if question is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return question


def question_create(question: QuestionModel, db: Session):
    question_tmp = question.dict()
    new_question = {
        **question_tmp,
        "general": json.dumps(question_tmp["general"], ensure_ascii=False),
        "content": json.dumps(question_tmp["content"], ensure_ascii=False),
    }
    return create_question(new_question, db)


def question_update(id: str, question: QuestionUpdateModel, db: Session):
    question_tmp = question.dict()
    new_question = {
        **question_tmp,
        "general": json.dumps(question_tmp["general"], ensure_ascii=False),
        "content": json.dumps(question_tmp["content"], ensure_ascii=False),
    }
    return update_question(id, new_question, db)


def update_question_test(id: str, db: Session):
    return update_question_test_option(id, db)
