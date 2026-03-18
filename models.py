from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# Creamos la clase que representa la tabla en la base de datos
class TareaDB(Base):
    __tablename__ = "tareas" # Nombre de la tabla en SQLite

    # Definimos las columnas
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, nullable=True) # nullable=True significa que puede estar vacío
    completada = Column(Boolean, default=False)