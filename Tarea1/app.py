import web

urls = (
    '/', 'contenedor.metodos.Index',
    '/docker', 'contenedor.metodos.Docker',
    '/ubuntu', 'contenedor.metodos.Ubuntu'
    )
    
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()