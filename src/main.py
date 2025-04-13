#IMPORTAR LIBRERIAS 
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


#CONFIGURACION DE LA APP
application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type' 


#CONFIGURACION DE LA PAGINA
@application.route("/api")
def inicio():
    return abrir_html()

#ABRIR EL HTML 
def abrir_html():
    try:
        with open("src/index.html", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<bold>Error 404 </bold>"

# RUTA PARA AGREGAR 