from fastapi import APIRouter, Depends
from app.api.hsk.services import hsk
from app.config.hsk.database import get_db
from sqlalchemy.orm import Session
from app.api.hsk.repository.question.model import QuestionModel, QuestionUpdateModel
router = APIRouter(prefix="/hsk")


@router.put("/",
            tags=["Migii API"],
            description="Update question test by id",
            summary="Migii",
            )
def hsk_update_question_test(id: str = None, db: Session = Depends(get_db)):
    return hsk.update_question_test(id, db)
