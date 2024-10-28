from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia estos valores con tus credenciales de Clever Cloud
DATABASE_USER = "urhewtjnb9xrgqd6"
DATABASE_PASSWORD = "ed2yadnjkbbhGcAn9KvN"
DATABASE_HOST = "buoxwl7ia36piwbtmxtk-mysql.services.clever-cloud.com"
DATABASE_PORT = "3306"  # generalmente 3306 para MySQL
DATABASE_NAME = "buoxwl7ia36piwbtmxtk"

# Crear la cadena de conexión
connection_string = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Configurar el engine y la sesión
engine = create_engine(connection_string, pool_pre_ping=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#Esto no conecta inmediatamente con la db, hay que hacerlo aparte

#Creamos la sesion, que es la que nos permite realizar transacciones en la base de datos


