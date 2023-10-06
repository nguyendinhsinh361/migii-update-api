import json
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api.hsk.repository.question_test.model import QuestionTestEntity
from app.utils import helper
from app.api.hsk.repository.question.repo import get_question


def get_question_test(id: int, db: Session):
    return db.query(QuestionTestEntity).filter(QuestionTestEntity.id == id).first()


def get_all_question_test(db: Session):
    return db.query(QuestionTestEntity).all()


def update_question_test_detail(db: Session, question_test_detail):
    part_of_test = json.loads(question_test_detail.parts)
    groups_ids = helper.get_group_ids_of_question_test(part_of_test)
    for id in groups_ids:
        question_detail_from_db = get_question(int(id), db)
        if (not question_detail_from_db):
            continue
        question_detail_from_question_test = helper.find_object_by_id(
            part_of_test, id)

        if (not helper.are_values_equal(json.loads(question_detail_from_db.general), question_detail_from_question_test["general"]) or
           not helper.are_values_equal_content(json.loads(question_detail_from_db.content), question_detail_from_question_test["content"])):
            print(1111, question_test_detail.id, 1111, id)
            part_of_test = helper.update_value(part_of_test, id, json.loads(
                question_detail_from_db.general), json.loads(question_detail_from_db.content))
    question_test_detail.parts = json.dumps(part_of_test, ensure_ascii=False)
    db.commit()
    db.refresh(question_test_detail)
    return question_test_detail.as_dict()


def update_question_test_all(db: Session):
    all_question_test = get_all_question_test(db)
    result = []
    for tmp in all_question_test:
        result.append(update_question_test_detail(db, tmp))
    test = [tmp for tmp in result if tmp["id"] == 579][0]
    test["parts"] = json.loads(test["parts"])
    return test


def update_question_test_option(question_test_id: int, db: Session):
    if (question_test_id):
        question_test_detail = get_question_test(question_test_id, db)
        return update_question_test_detail(db, question_test_detail)
    return update_question_test_all(db)
