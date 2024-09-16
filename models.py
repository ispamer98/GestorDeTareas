
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime
import db

#Creamos la clase de Tarea
class Task(db.Base):
    __tablename__ = "tarea" #Le damos nombre a la tabla
    __table_args__ = {"sqlite_autoincrement": True} #Creamos una variable que se autoincrementa
    id = Column(Integer, primary_key=True) #Creamos la columna de ID
    content = Column(String, nullable=False) #Columna de contenido de tarea
    completed = Column(Boolean) #Y la que verifica si esta completada

    def __init__(self, content, completed):
        self.content = content
        self.completed = completed

    def __str__(self):
        return f"Tarea {self.id} : {self.content} ({self.completed})" #Devolvemos la info

#Creaamos la tabla de Comentarios
class Comment(db.Base):
    __tablename__ = "comentario" #Nombre de tabla
    __table_args__ = {"sqlite_autoincrement": True} #Variable que autoincrementa
    id = Column(Integer, primary_key=True) #Le damos una ID
    name = Column(String, nullable=False) #Nombre del creador de comentario
    comment = Column(String, nullable=False) #Contenido del comentario
    date = Column(String, nullable=False) #Fecha que añadiremos automaticamente

    def __init__(self, name, comment, date=None):
        self.name = name
        self.comment = comment
        self.date = date if date else datetime.now().strftime('%d / %m / %Y - %H:%M')
        #La fecha se creará automaticamente con la fecha del PC que cree el comentario

    def __str__(self):
        return f"Tarea {self.id} : {self.name} ({self.date})\n{self.comment}"
    #Y devolvemos la info del comentario

