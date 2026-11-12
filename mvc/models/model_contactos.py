import os
from supabase import create_client, Client
from dotenv import load_dotenv

import hashlib
import hmac
from typing import Any, cast
import logging

load_dotenv()

logger = logging.getLogger(__name__)

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase:Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
            self.SECRET_KEY = b"hola" 
        except Exception as error:
            print(f"ERROR 100: {error.arg[0]}")

    def generar_hash(self, id: int) -> str:
        try:
            """Genera un hash unico apartir de la ID"""
            mensaje = str(id). enconde("utf-8")
            firma = hmac.new(self.SECRET_KEY, mensaje, hashlib.sha256).hexdigest()
            return f"{id}:{firma}"
        except Exception as error:
            print(f"ERROR 106: {str(error)}")
            return ""

    def validar_hash(self, hash_a_validar: str) -> int|None:
        try:
            id_str, sep, _ = hash_a_validar.partition(":")
            resultado_id = None

            if sep and id_str.isdigit():
                token_esperado = self.generar_hash(int(id_str))
                if hmac.compare_digest(token_esperado, hash_a_validar):
                    resultado_id = int(id_str)
                else:
                    resultado_id = None
            else:
                resultado_id = None

            return resultado_id

        except Exception as error:
            print(f"ERROR 107: {str(error)}")
            return -1

    def obtenerContactos(self) -> list[dict[str,Any]]:
        contactos: list[dict[str, Any]]
        try:
            #SELECT * FROM contactos;
            response = self.supabase.table("contactos").select("*").execute()
            return response.data
        except Exception as error:
            logger.error("ERROR 101: %s", error)
            print("ERROR 101: {str{error}}")
            return []

    def buscarContacto(self, id_contacto:int):
        response = self.supabase.table("contactos").select("*").eq("id", id_contacto).execute()
        return response.data[0]

    def insertarContacto(self, nombre:str, email:str, telefono:str):
        datos = {
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").insert(datos).execute()
        return response.data

    def borrarContacto(self, id_contacto:int):
        response = self.supabase.table("contactos").delete().eq("id", id_contacto).execute()
        return response.data

    def actualizarContacto(self, id_contacto:int, nombre:str, email:str, telefono:str):
        datos_nuevos = {
            "id": id_contacto,
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }
        response = self.supabase.table("contactos").update(datos_nuevos).eq("id", id_contacto).execute()
        return response.data

if __name__ == "__main__":
    model_contactos = ModelContactos()
    print(model_contactos.obtenerContactos())
    print(model_contactos.buscarContacto(2))
    print(model_contactos.insertarContacto("uriel","uriel@gmail.com", "1414141414"))
    print(model_contactos.borrarContacto(1))
    print(model_contactos.actualizarContacto(4, "OSCAR", "oscar@gmail.com", "1515151515"))
