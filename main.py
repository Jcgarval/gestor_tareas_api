from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional

# Importamos la configuración de nuestra base de datos
from database import engine, SessionLocal
import models

# 1. Esta línea mágica crea el archivo 'tareas.db' y las tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Gestor de Tareas")

# 2. Actualizamos el modelo Pydantic. 
# Ya no pedimos el 'id' al crear, porque la base de datos lo generará automáticamente.
class TareaCreate(BaseModel):
    titulo: str
    descripcion: Optional[str] = None
    completada: bool = False

class TareaUpdate(BaseModel):
    titulo: Optional[str] = None
    descripcion: Optional[str] = None
    completada: Optional[bool] = None

# 3. Función para abrir y cerrar la conexión a la base de datos en cada petición
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 4. Ruta para crear una tarea en la base de datos real
@app.post("/tareas")
def crear_tarea(tarea: TareaCreate, db: Session = Depends(get_db)):
    # Transformamos los datos de Pydantic al formato de SQLAlchemy
    nueva_tarea = models.TareaDB(
        titulo=tarea.titulo, 
        descripcion=tarea.descripcion, 
        completada=tarea.completada
    )
    db.add(nueva_tarea) # Preparamos la tarea
    db.commit()         # Guardamos en la base de datos
    db.refresh(nueva_tarea) # Obtenemos el ID que se le ha asignado
    return nueva_tarea

# 5. Ruta para leer todas las tareas de la base de datos real
@app.get("/tareas")
def obtener_tareas(db: Session = Depends(get_db)):
    # Hacemos una consulta (query) a la tabla TareaDB
    tareas = db.query(models.TareaDB).all()
    return tareas

# 6. Ruta para buscar una tarea por ID en la base de datos:
@app.get("/tareas/{tarea_id}")
def obtener_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()

    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return tarea

# 7. Ruta para borrar una tarea de la base de datos:
@app.delete("/tareas/{tarea_id}")
def eliminar_tarea(tarea_id: int, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()

    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    db.delete(tarea) # Preparamos la eliminación
    db.commit()      # Guardamos los cambios en la base de datos
    return {"mensaje": f"Tarea {tarea_id} eliminada exitosamente"}

# 8. Ruta para actualizar una tarea
@app.put("/tareas/{tarea_id}")
def actualizar_tarea(tarea_id: int, tarea_actualizada: TareaUpdate, db: Session = Depends(get_db)):
    tarea = db.query(models.TareaDB).filter(models.TareaDB.id == tarea_id).first()

    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    
    # Actualizamos solo los campos que el usuario ha enviado 
    if tarea_actualizada.titulo is not None:
        tarea.titulo = tarea_actualizada.titulo
    if tarea_actualizada.descripcion is not None:
        tarea.descripcion = tarea_actualizada.descripcion
    if tarea_actualizada.completada is not None:
        tarea.completada = tarea_actualizada.completada

    db.commit()      # Guardamos los cambios en la base de datos
    db.refresh(tarea) # Obtenemos la versión actualizada de la tarea
    return tarea