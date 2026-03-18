# 📝 Gestor de Tareas API RESTful

Una API RESTful completa para la gestión de tareas, construida con Python y FastAPI. Este proyecto demuestra la implementación de operaciones CRUD, conexión a base de datos relacional y buenas prácticas de desarrollo backend.

## 🚀 Tecnologías utilizadas
* **Framework:** FastAPI
* **Base de datos:** SQLite
* **ORM:** SQLAlchemy
* **Validación de datos:** Pydantic
* **Servidor:** Uvicorn

## ⚙️ Instalación y ejecución local

Sigue estos pasos para probar la API en tu propio equipo:

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/Jcgarval/gestor_tareas_api.git](https://github.com/Jcgarval/gestor_tareas_api.git)
   cd gestor_tareas_api

2. **Crea y activa un entorno virtual:**
     python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate

3. **Instala las dependencias:**
   pip install -r requirements.txt

4. **Inicia el servidor local:**
   uvicorn main:app --reload


Una vez que el servidor esté corriendo, FastAPI genera automáticamente la documentación de la API. Puedes interactuar con ella de forma visual entrando a:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc