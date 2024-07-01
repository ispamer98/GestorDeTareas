
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime
import db

class Task(db.Base):
    __tablename__ = "tarea"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)
    content = Column(String, nullable=False)
    completed = Column(Boolean)

    def __init__(self, content, completed):
        self.content = content
        self.completed = completed

    def __str__(self):
        return f"Tarea {self.id} : {self.content} ({self.completed})"

class Comment(db.Base):
    __tablename__ = "comentario"
    __table_args__ = {"sqlite_autoincrement": True}
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    date = Column(String, nullable=False)

    def __init__(self, name, comment, date=None):
        self.name = name
        self.comment = comment
        self.date = date if date else datetime.now().strftime('%d / %m / %Y - %H:%M')

    def __str__(self):
        return f"Tarea {self.id} : {self.name} ({self.date})\n{self.comment}"

