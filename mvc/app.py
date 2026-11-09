import web
from controllers.index import Index
from controllers.contactos import Contactos
from controllers.insertar_contacto import Insertar_contacto

urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
    '/insertar_contacto', 'Insertar_contacto',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()