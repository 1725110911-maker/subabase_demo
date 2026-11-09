import web
from models.model_contactos import ModelContactos
render = web.template.render('views/', base='template')

class Borrar_contacto:
    def GET(self, id_contacto):
        return render.borrar_contacto(id_contacto)
