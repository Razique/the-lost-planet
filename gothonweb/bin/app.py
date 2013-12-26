import sys
sys.path.append('../')
import web
from gothonweb import map

web.config.debug = False

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)
app = web.application(urls, globals())

if web.config.get('__session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config.__session = session
else:
    session = web.config.__session

render = web.template.render('templates/', base='layout')


class Index(object):
    @staticmethod
    def GET():
        session.room = map.START
        web.seeother("/game")


class GameEngine(object):
    @staticmethod
    def GET():
        if session.room:
            return render.show_room(room=session.room)
        else:
            return render.you_died()

    @staticmethod
    def POST():
        form = web.input(action=None)

        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")


if __name__ == "__main__":
    app.run()