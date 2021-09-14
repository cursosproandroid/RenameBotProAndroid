# Cursos Pro Android by Skueletor ©️ 2021
import os

class Config(object):

    #Obtén el token desde @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    #Las cosas de la API de Telegram
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    #Obtén estos valores desde my.telegram.org

    #Este es el apartado para almacenar usuarios que están autorizados a usar el bot como administrador
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    #Este apartado es para banear a los miembros no deseados
    BANNED_USERS = []

    #La ubicación de descarga, donde se ejecuta el servidor HTTP (no toques nada aquí)
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    #El tamaño máximo de Telegram para subir los archivos (no toques nada aquí)
    TG_MAX_FILE_SIZE = 2097152000

    #Tamaño del fragmento que debe usarse con las solicitudes
    CHUNK_SIZE = 128

    #URL de la base de datos
    DB_URI = os.environ.get("DATABASE_URL", "")
