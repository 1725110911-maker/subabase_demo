import web
from models.model_contactos import ModelContactos
render = web.template.render('views/', base='template')

class Actualizar_contacto:

    def GET(self, id_contacto):
        model_contactos = ModelContactos()
        contacto = model_contactos.buscarContacto(id_contacto)
        print(contacto)
        return render.actualizar_contacto(contacto)
