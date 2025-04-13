#IMPORTAR LIBRERIAS 
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


#CONFIGURACION DE LA APP
application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type' 


#CONFIGURACION DE LA PAGINA
@application.route("/api", methods=["GET"])
def inicio():
    return abrir_html()

#ABRIR EL HTML 
def abrir_html():
    try:
        with open("src/index.html", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<bold>Archivo no encontrado</bold>"

# RUTA PARA AGREGAR LA CATEGORIA
@application.route("/api/agregar_categoria", methods=["POST"])
def agregar_categoria():
    #RECOGEMOS LOS DATOS DEL FORMULARIO ENVIADO 
    BLABLA = request.form.get("BLABLA")
    BLABLA = request.form.get("BLABLA")
    BLABLA = request.form.get("BLABLA")
    BLABLA = request.form.get("BLABLA")
