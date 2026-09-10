import json


class ArchivoServicio:

    def leer_json(self, ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)