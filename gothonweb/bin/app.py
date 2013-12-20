import web

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")


class Index:
    def __init__(self):
        pass

    @staticmethod
    def GET():
        return render.hello_form()

    @staticmethod
    def POST():
        form = web.input(name=None, greet=None)
        greetings = "%s, %s" % (form.name, form.greet)
        x = web.input(myfile={})
        filedir = 'upload'

        if 'myfile' in x:
            try:
                filepath = x.myfile.filename.replace('\\', '/')
                filename = filepath.split('/')[-1]  # splits the and chooses the last part (the filename with extension)
                fout = open(filedir + '/' + filename, 'w')  # creates the file where the uploaded file should be stored
                fout.write(x.myfile.file.read())  # writes the uploaded file to the newly created file.
                fout.close()  # closes the file, upload complete.
                return render.index(greetings)
            except IOError:
                return render.index(greetings)
        else:
            raise web.seeother('/hello')


if __name__ == "__main__":
    app.run()
