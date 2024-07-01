#Engine es el que permite a SQLALchemy conectarse a la base de datos y hablar en un dialecto concreto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///database/tasks.db",
                       connect_args={"check_same_thread":False})
                        #Hace que no compruebe desde que hilo se ejecuta, ya que al utilizar
                        #Flask, la ejecución la hace toda en un solo hilo.


#Cada clase creada en el archivo models.py, al añadirle esta variable, se encargara de
#mapear y vincular cada clase a una tabla.
Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()


#Esto no conecta inmediatamente con la db, hay que hacerlo aparte

#Creamos la sesion, que es la que nos permite realizar transacciones en la base de datos


