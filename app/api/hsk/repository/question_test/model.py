from datetime import datetime
from sqlalchemy import JSON, Column, DateTime, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional, List

from app.config.hsk.database import DATABASE_URL
Base = declarative_base()


class QuestionTestEntity(Base):
    __tablename__ = 'questions_test'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    parts = Column(String)
    level = Column(Integer)
    groups = Column(String)
    score = Column(Integer)
    active = Column(Integer)
    pass_score = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    time = Column(Integer)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


# Tạo đối tượng `engine` để kết nối với cơ sở dữ liệu MySQL
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)
