import web
render = web.template.render('views', base='template')

class Index:

    def GET(self):
        return render.index()
