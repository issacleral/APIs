# **Documentación de la API**

## **Descripción**
Esta API está desarrollada en Flask y permite gestionar diferentes rutas, incluyendo la visualización de una página HTML y la adición de categorías mediante un formulario. Además, utiliza CORS para manejar solicitudes desde diferentes orígenes.

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
3. Abre tu navegador y accede a `http://127.0.0.1:5000/api`.

---

## **Rutas Disponibles**

### **1. `/api`**
- **Método**: `GET`
- **Descripción**: Renderiza la página principal (`index.html`).
- **Respuesta**: Devuelve el contenido del archivo HTML.

### **2. `/api/agregar_categoria`**
- **Método**: `POST`
- **Descripción**: Permite agregar una categoría mediante un formulario.
- **Parámetros**:
  - `BLABLA`: Datos enviados desde el formulario.
- **Respuesta**: (Actualmente no implementada completamente).

---
