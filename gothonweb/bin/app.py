import sys
sys.path.append('../')
import web
import glob
import random
from gothonweb import map, game_lexicon

web.config.debug = False

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)
app = web.application(urls, globals())

if web.config.get('__session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None, 'attempts': None, 'user': None})
    web.config.__session = session
else:
    session = web.config.__session

render = web.template.render('templates/', base='layout')


class Index(object):
    @staticmethod
    def GET():
        session.room = map.START
        session.attempts = 5
        if session.user:
            web.seeother("/game")
        else:
            return render.intro()


class GameEngine(object):
    def __init__(self):
        pic = glob.glob("static/*.jpg")
        random_pic = random.choice(pic)
        self.lexicon = game_lexicon.AssertLexicon()
        self.view = render.show_room(room=session.room, picture=random_pic,
                                     attempts=session.attempts, user=session.user)

    def GET(self):
        if session.room:
            user_data = web.input(action=None)
            if user_data.action:
                session.room = session.room.go(user_data.action)
                web.seeother("/game")
            else:
                return self.view
        else:
            return render.you_died()

    def POST(self):
        if session.user is None:
            # Username init
            user = web.input(username=None)
            session.user = user.username
            web.seeother("/game")

        code = web.input(armory_code=None)
        process = web.input(action=None)
        if process.action:
            if self.lexicon.lexicon(process.action, session.room.name, test=False) is not False:
                session.room = session.room.go(self.lexicon.lexicon(process.action, session.room.name, test=False))
                web.seeother("/game")
            else:
                return render.you_died()
        elif code.armory_code:
            if session.attempts != 1:
                if self.lexicon.lexicon(code.armory_code, session.room.name, test=False) is False:
                    session.attempts -= 1
                else:
                    session.room = session.room.go(code.armory_code)
                web.seeother("/game")
            else:
                return render.you_died()
        else:
            return self.view

#TODO: Map selector
#TODO: Help System
if __name__ == "__main__":
    app.run()