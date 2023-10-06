from datetime import datetime
from sqlalchemy import JSON, Column, DateTime, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional, List

from app.config.hsk.database import DATABASE_URL
Base = declarative_base()


class LanguageModel(BaseModel):
    vi: str
    en: str


class GeneralModel(BaseModel):
    G_text: list
    G_text_translate: LanguageModel
    G_text_audio: str
    G_text_audio_translate: LanguageModel
    G_audio: list
    G_image: list[str]


class ContentModel(BaseModel):
    Q_text: str
    Q_audio: str
    Q_image: str
    A_text: list[int]
    A_audio: list
    A_image: list
    A_correct: list[int]
    explain: LanguageModel


class QuestionModel(BaseModel):
    title: str
    general: GeneralModel
    content: list[ContentModel]
    level: int
    level_of_difficult: int
    kind: str
    correct_answers: str
    check_admin: int
    count_question: int
    tag: str
    score: int
    created_at: datetime
    updated_at: datetime
    check_explain: int
    title_trans: str
    source: str
    score_difficult: float


class QuestionUpdateModel(BaseModel):
    # title: Optional[str]
    general: Optional[GeneralModel]
    content: Optional[list[ContentModel]]
    # level: Optional[int]
    # level_of_difficult: Optional[int]
    # kind: Optional[str]
    # correct_answers: Optional[str]
    # check_admin: Optional[int]
    # count_question: Optional[int]
    # tag: Optional[str]
    # score: Optional[int]
    # created_at: Optional[datetime]
    # updated_at: Optional[datetime]
    # check_explain: Optional[int]
    # title_trans: Optional[str]
    # source: Optional[str]
    # score_difficult: Optional[float]


class QuestionEntity(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    general = Column(String)
    content = Column(String)
    level = Column(Integer)
    level_of_difficult = Column(Integer)
    kind = Column(String)
    correct_answers = Column(String)
    check_admin = Column(Integer)
    count_question = Column(Integer)
    tag = Column(String)
    score = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    check_explain = Column(Integer)
    title_trans = Column(String)
    source = Column(String)
    score_difficult = Column(Float)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# Tạo đối tượng `engine` để kết nối với cơ sở dữ liệu MySQL
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)
