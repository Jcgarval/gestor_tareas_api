from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Le decimos dónde guardar el archivo de la base de datos
URL_BASE_DATOS = "sqlite:///./tareas.db"

# 2. Creamos el "motor", que es el encargado de conectarse a SQLite
engine = create_engine(
    URL_BASE_DATOS, 
    connect_args={"check_same_thread": False} # Esto es un requisito específico de SQLite en FastAPI
)

# 3. Creamos una "sesión", que es como la ventanilla de atención al cliente para pedirle cosas a la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Creamos una clase Base. Todos nuestros modelos de datos heredarán de ella
Base = declarative_base()