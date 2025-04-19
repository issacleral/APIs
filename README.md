# **Documentación de la API**

## **Descripción**
Esta API está desarrollada en Flask y permite gestionar diferentes rutas, incluyendo la visualización de una página HTML, la conexión a una base de datos SQLite, la búsqueda de categorías y la adición de nuevas películas mediante un formulario. Además, utiliza CORS para manejar solicitudes desde diferentes orígenes.

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

## **URL**
1. **http://127.0.0.1:5000/**

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
## **Base De Datos**
```sql

  CREATE TABLE peliculas (
      id INTEGER PRIMARY KEY,
      titulo VARCHAR(10),
      duracion SMALLINT,
      fecha_estreno DATE
  );


  INSERT INTO peliculas (id, titulo, duracion, fecha_estreno) VALUES
  (1, 'Parasite', 97, '2019-12-03'),
  (2, 'Enemigo al acecho', 130, '2009-04-25'),
  (3, 'American Paradise', 141, '2002-12-01'),
  (4, 'Antes que anochezca', 102, '2007-11-04'),
  (5, 'Inglorious Bastards', 105, '2009-08-13'),
  (6, 'Training Day', 135, '2001-01-18'),
  (7, 'Pedro Navaja', 114, '1984-10-03'),
  (8, 'Gladiator', 215, '2000-04-10'),
  (9, 'The Patriot', 182, '1995-06-21');

  SELECT * FROM peliculas;
```

---

## **Rutas Disponibles**

### **1. `/`**
- **Método**: `GET`
- **Descripción**: Renderiza la página principal (`index.html`).
- **Respuesta**: Devuelve el contenido del archivo HTML o un mensaje de error si el archivo no se encuentra.

---

### **2. `/agregar`**
- **Método**: `POST`
- **Descripción**: Permite agregar una nueva película a la base de datos.
- **Parámetros**:
  - `titulo`: Título de la película.
  - `duracion`: Duración de la película (en minutos).
  - `fecha_estreno`: Fecha de estreno de la película.
- **Respuesta**:
  - Si los datos son válidos: `"Película agregada correctamente."`
  - Si faltan datos: `"Error: Todos los campos son requeridos"`

---

### **3. `/search`**
- **Método**: `GET`
- **Descripción**: Permite buscar categorías basándose en un parámetro de consulta.
- **Parámetros**:
  - `query`: El término de búsqueda proporcionado por el usuario.
- **Respuesta**:
  - Si no se proporciona un término de búsqueda: `"No hay datos que buscar"`
  - Si se proporciona un término de búsqueda: `"Resultados de la búsqueda <query>"`

---

### **4. `/peliculas`**
- **Método**: `GET`
- **Descripción**: Conecta a la base de datos SQLite y ejecuta una consulta para obtener todas las películas.
- **Respuesta**: Devuelve los resultados de la consulta en formato JSON.

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
  - `/agregar`: Permite agregar una nueva película.
  - `/search`: Permite realizar búsquedas basadas en un parámetro.
  - `/peliculas`: Ejecuta una consulta en la base de datos SQLite para obtener todas las películas.

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