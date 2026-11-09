import web 
from models.model_contactos import ModelContactos
render = web.template.render('views/', base='template')

class Insertar_contacto:

    def GET(self):
        return render.insertar_contacto()

    def POST(self):
        formulario = web.input()
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']

        print("Nombre: ", nombre)
        print("Email: ", email)
        print("Teléfono: ", telefono)

        model_contactos = ModelContactos()
        datos = model_contactos.insertarContacto(nombre, email, telefono)

        print(datos)
        web.header('Content-Type', 'text/html')
        html = """
                <h1>Contacto almacenado correctamente</h1>
                <a href="/contactos">Volver a Contactos</a>
        """

        return html
