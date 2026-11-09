import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos:

    def __init__(self) -> None:
        try:
            self.supabase:Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            print(f"ERROR 100: {error.arg[0]}")

    def obtenerContactos(self):
        #SELECT * FROM contactos;
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

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
