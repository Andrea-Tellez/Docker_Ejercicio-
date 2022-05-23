import web

indexx = web.template.render('contenedor/')
docker = web.template.render('contenedor/')
ubuntu = web.template.render('contenedor/')

class Index:
    def GET(self):
        return indexx.index()
    
class Docker:
    def GET(self):
        return docker.docker()

class Ubuntu:
    def GET(self):
        return ubuntu.ubuntu()