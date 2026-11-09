import web
from models.model_contactos import ModelContactos
render = web.template.render('views/', base='template')

class Contactos:

    def GET(self):

        model_contactos = ModelContactos()
        datos = model_contactos.obtenerContactos()

        print (datos)
        return render.contactos(datos)
