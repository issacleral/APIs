# **Documentación de la API**

## **Descripción**
Esta API está desarrollada en Flask y permite gestionar diferentes rutas, incluyendo la visualización de una página HTML, la conexión a una base de datos SQLite, la búsqueda de categorías y la edición de nuevas categorías mediante un formulario. Además, utiliza CORS para manejar solicitudes desde diferentes orígenes.

---

## **Estructura del Proyecto**
```
APIs/
├── src/
│   ├── main.py               # Código principal de la API
│   ├── templates/            # Carpeta para los archivos HTML
│   │   └── index.html        # Página principal de la API
├── README.md                 # Documentación del proyecto
```

---

## **Requisitos Previos**
1. **Python**: Asegúrate de tener Python instalado (versión 3.7 o superior).
2. **Entorno Virtual**: Se recomienda usar un entorno virtual para instalar las dependencias.

---

## **Instalación**
1. Clona el repositorio o descarga los archivos del proyecto.
2. Crea un entorno virtual:
   ```bash
   python -m venv env
   ```
3. Activa el entorno virtual:
   - En Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     source env/bin/activate
     ```
4. Instala las dependencias necesarias:
   ```bash
   pip install flask flask-cors
   ```

---

## **Ejecución**
1. Navega al directorio `src`:
   ```bash
   cd src
   ```
2. Ejecuta el servidor Flask:
   ```bash
   flask --app main.py --debug run
   ```
3. Abre tu navegador y accede a `http://127.0.0.1:5000`.

---

## **Rutas Disponibles**

### **1. `/`**
- **Método**: `GET`, `POST`
- **Descripción**: Renderiza la página principal (`index.html`).
- **Respuesta**: Devuelve el contenido del archivo HTML o un mensaje de error si el archivo no se encuentra.

---

### **2. `/conexion`**
- **Método**: `GET`
- **Descripción**: Conecta a la base de datos SQLite y ejecuta una consulta para obtener todas las clases.
- **Respuesta**: Devuelve los resultados de la consulta en formato JSON.

---

### **3. `/search`**
- **Método**: `GET`
- **Descripción**: Permite buscar categorías basándose en un parámetro de consulta.
- **Parámetros**:
  - `query`: El término de búsqueda proporcionado por el usuario.
- **Respuesta**:
  - Si no se proporciona un término de búsqueda: `"No hay datos que buscar"`.
  - Si se proporciona un término de búsqueda: `"Resultados de la búsqueda <query>"`.

---

### **4. `/`**
- **Método**: `POST`
- **Descripción**: Permite agregar una nueva categoría mediante un formulario.
- **Parámetros**:
  - `titulo`: Título de la categoría.
  - `duracion`: Duración de la categoría.
  - `fecha_estreno`: Fecha de estreno de la categoría.
- **Respuesta**: (Actualmente no implementada completamente).

---

## **Configuración del Proyecto**
### **CORS**
Se utiliza `flask-cors` para permitir solicitudes desde diferentes orígenes. La configuración está definida en el archivo `main.py`:
```python
from flask_cors import CORS
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'
```

### **Renderización de HTML**
El archivo HTML se renderiza utilizando la función `open`. Asegúrate de que los archivos HTML estén en la carpeta `templates`.

---

## **Estructura del Código**
### **Archivo `main.py`**
- **Configuración de la aplicación**:
  ```python
  application = Flask(__name__)
  cors = CORS(application)
  application.config['CORS_HEADERS'] = 'Content-Type'
  ```
- **Rutas principales**:
  - `/`: Renderiza el archivo `index.html`.
  - `/conexion`: Ejecuta una consulta en la base de datos SQLite.
  - `/search`: Permite realizar búsquedas basadas en un parámetro.
  - `/api/agregar_categoria`: Recibe datos de un formulario para agregar una categoría.

---

## **Notas**
- Si el archivo `index.html` no se encuentra, se devuelve un mensaje de error: `"<bold>Archivo no encontrado</bold>"`.
- Asegúrate de que el archivo `index.html` esté ubicado en la carpeta `templates`.

---

## **Comandos Útiles**
- **Activar entorno virtual**:
  ```bash
  .\env\Scripts\activate
  ```
- **Ejecutar el servidor Flask**:
  ```bash
  flask --app main.py --debug run
  ```

---