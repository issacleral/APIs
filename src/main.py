#IMPORTAR LIBRERIAS 
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


#CONFIGURACION DE LA APP
application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type' 


#CONFIGURACION DE LA PAGINA
@application.route("/", methods=["GET", "POST"])
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
@application.route("/conexion", methods=["GET"])
def conexion():
    conexion = SQLiteConnection("Database1.db")
    classes = conexion.execute_query("SELECT * FROM clases ")
    return classes

#  BUSCADOR DE CATEGORIAS 
@application.route("/search", methods=["GET"])
def buscador():
    datos_usuario = request.args.get("query")

    if datos_usuario is None:
        return "No hay datos que buscar"
       
    return "Resultados de la busqueda " + str(datos_usuario)

# RUTA PARA AGREGAR LA CATEGORIA
@application.route("/api/agregar_categoria", methods=["POST"])
def agregar_categoria():
    #RECOGEMOS LOS DATOS DEL FORMULARIO ENVIADO 
    BLABLA = request.form.get("BLABLA")
    BLABLA = request.form.get("BLABLA")
    BLABLA = request.form.get("BLABLA")
    BLABLA = request.form.get("BLABLA")