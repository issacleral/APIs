#IMPORTAR LIBRERIAS 
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


#CONFIGURACION DE LA APP
application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type' 


#CONFIGURACION DE LA PAGINA
@application.route("/", methods=["GET"])
def inicio():
    return abrir_html()

#ABRIR EL HTML 
def abrir_html():
    try:
        with open("index.html", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<bold>Archivo no encontrado</bold>"
    

# CONEXION A LA BASE DE DATOS
@application.route("/conexion", methods=["GET", "POST"])
def conexion():
    conexion = SQLiteConnection("Database1.db")
    classes = conexion.execute_query("SELECT * FROM peliculas ")
    return classes

#  BUSCADOR DE CATEGORIAS 
@application.route("/search", methods=["GET", "POST"])
def buscador():
    datos_usuario = request.args.get("query")

    if datos_usuario is None:
        return "No hay datos que buscar"
       
    return "Resultados de la busqueda " + str(datos_usuario)

# RUTA PARA AGREGAR LA CATEGORIA
@application.route("/agregar_categoria", methods=["GET", "POST"])
def agregar_categoria():
    #RECOGEMOS LOS DATOS DEL FORMULARIO ENVIADO 
    titulo = request.form.get("titulo")
    duracion = request.form.get("duracion")
    fecha_estreno = request.form.get("fecha_estreno")


 # VALIDAMOS LOS CAMPOS QUE NO ESTEN VACIOS EN EL FORMULARIO

    if not (titulo or duracion or fecha_estreno):
        return "Error: Todos los campos son requeridos"
    conexion = SQLiteConnection("Database1.db")

    conexion.execute_query(
        "INSERT INTO peliculas(titulo, duracion, fecha_estreno) VALUES (?, ?, ?)",
        [titulo, duracion, fecha_estreno],
        commit = True
    )
    
 
    return "Película agregada correctamente."

if __name__ == "__main__":
    application.run(debug=True)