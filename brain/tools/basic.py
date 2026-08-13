from datetime import datetime


def obtener_hora():
    return datetime.now().strftime("%H:%M")
