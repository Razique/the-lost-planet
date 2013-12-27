import sys
sys.path.append('../')
import web
import glob
import random
from gothonweb import map
from gothonweb import game_lexicon

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
        user_data = web.input(action=None)
        if session.room:
            # We generate an images random picker
            pic = glob.glob("static/*.jpg")
            random_pic = random.choice(pic)
            actions = game_lexicon.ListActions()
            # If the user has made a choice
            if user_data.action:
                session.room = session.room.go(user_data.action)
                web.seeother("/game")
            else:
                # TODO: Implement code input for the armory
                return render.show_room(room=session.room, picture=random_pic,
                                        actions=actions.actions(session.room.name))
        else:
            return render.you_died()


if __name__ == "__main__":
    app.run()