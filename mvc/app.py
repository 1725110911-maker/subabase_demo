import web
from controllers.index import Index
from controllers.contactos import Contactos
from controllers.insertar_contacto import Insertar_contacto
from controllers.actualizar_contacto import Actualizar_contacto
from controllers.borrar_contacto import Borrar_contacto
from controllers.ver_contacto import VerContacto
urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
    '/insertar_contacto', 'Insertar_contacto',
    '/actualizar_contacto/(.*)', 'Actualizar_contacto',
    '/borrar_contacto/(.*)', 'Borrar_contacto',
    '/ver_contacto/(.*)', 'VerContacto',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()