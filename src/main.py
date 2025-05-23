#IMPORTAR LIBRERIAS 
from flask import Flask, request
from flask_cors import CORS
from JGVutils import SQLiteConnection


#CONFIGURACION DE LA APP
application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type' 


#CONFIGURACION DE LA PAGINA DE INICIO
@application.route("/", methods=["GET"])
def inicio():
    # LEEMOS EL ARCHIVO HTML Y LO RETORNAMOS COMO RESPUESTA
    try:
        with open("html/index.html", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<bold>Archivos no encontrados</bold>"

#  BUSCADOR DE CATEGORIAS 
@application.route("/search", methods=["GET", "POST"])
def buscador():
    datos_usuario = request.args.get("query")

    if datos_usuario is None:
        return "No hay datos que buscar"
       
    return "Resultados de la busqueda " + str(datos_usuario)


# RUTA PARA AGREGAR UNA NUEVA PELICULA
@application.route("/agregar", methods=["POST"])
def agregar_pelicula():
    #RECOGEMOS LOS DATOS DEL FORMULARIO ENVIADO 
    titulo = request.form.get("titulo")
    duracion = request.form.get("duracion")
    fecha_estreno = request.form.get("fecha_estreno")


 # VALIDAMOS LOS CAMPOS QUE NO ESTEN VACIOS EN EL FORMULARIO

    if not (titulo and duracion and fecha_estreno):
        return "Error Los campos son requeridos"
    conexion = SQLiteConnection("Database1.db")

    conexion.execute_query(
        "INSERT INTO peliculas(titulo, duracion, fecha_estreno) VALUES (?, ?, ?)",
        [titulo, duracion, fecha_estreno],
        commit = True
    )
    
 
    return "<bold>Película agregada correctamente.</bold>"

if __name__ == "__main__":
    application.run(debug=True)



# CONEXION A LA BASE DE DATOS
@application.route("/peliculas", methods=["GET"])
def conexion():
    conexion = SQLiteConnection("Database1.db")
    peliculas = conexion.execute_query("SELECT * FROM peliculas ")
    return peliculas