from random import sample
from werkzeug.utils import secure_filename 
import os

def generar_cadena_aleatoria():
    #Generando string aleatorio
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio

def guardar_archivo_upload(archivo):
    basepath = os.path.dirname(__file__)
    basepath = os.path.dirname(basepath)
    static_folder = os.path.join(basepath, "static")

    # Ubicar la carpeta "upload" dentro de "static" y verificar si existe, si no, crearla
    upload_folder = os.path.join(static_folder, "upload")
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Si no se envió un archivo, usar la imagen por defecto 'default.jpg'
    if archivo is None or archivo.filename == '':
        return 'default.jpg'

    # Obtener el nombre seguro del archivo y generar un nuevo nombre aleatorio con extensión
    filename = secure_filename(archivo.filename)
    extension = os.path.splitext(filename)[1]
    nuevo_nombre_archivo = generar_cadena_aleatoria() + extension
    upload_path = os.path.join(upload_folder, nuevo_nombre_archivo)
    archivo.save(upload_path)
    return nuevo_nombre_archivo