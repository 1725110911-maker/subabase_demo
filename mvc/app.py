import web
from controllers.index import Index
from controllers.contactos import Contactos

urls = (
    '/', 'Index',
    '/contactos', 'Contactos',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()