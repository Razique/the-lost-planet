import sys
sys.path.append('../')
import web
import glob
import random
import hashlib
import logging
import db_controllers

from gothonweb import map, game_lexicon
from sanitize import sanitize

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

web.config.debug = False

# Routes definition
urls = (
    '/', 'Index',
    '/game', 'GameEngine',
    '/rooms', 'Rooms',
    '/login', 'Login',
    '/logout', 'Logout',
)
app = web.application(urls, globals())

if web.config.get('__session') is None:
    store = web.session.DiskStore('sessions')
    # Session init
    session = web.session.Session(app, store, initializer={'room': None, 'attempts': None, 'user': None,
                                                           'logged': None})
    web.config.__session = session
else:
    session = web.config.__session

# Template definition
render = web.template.render('templates/', base='layout')


class Index(object):
    def __init__(self):
        pass

    @staticmethod
    def GET():
        session.room = map.START
        session.attempts = 5
        return render.intro(display="none", message=None)


class Login(object):
    def __init__(self):
        self.display = "block"
        self.message_user_already_exists = "Sorry! This user already exists; please try again."
        self.message_user_not_found = "Sorry! This user has not been found. Please try again."

    @staticmethod
    def GET():
        web.seeother("/")

    def POST(self):
        user = web.input(username=None)
        password = web.input(password=None)
        resume = web.input(resume=None)

        # Data sanitizing
        c_user = sanitize(user.username)
        c_password = hashlib.md5(sanitize(password.password)).hexdigest()

        if not resume.resume:
            # New user
            if user.username and password.password:
                # Does the user already exist?
                if db_controllers.user_exists(c_user, c_password) is False:
                    return render.intro(self.display, self.message_user_already_exists)
                else:
                    # User creation
                    db_controllers.create_user(c_user, c_password)
                    session.logged = True
                    session.user = c_user
                    # We redirect the user
                    web.seeother("/rooms")
        else:
            # Does the user exist?
            if db_controllers.user_exists(c_user, c_password) is False:
                session.logged = True
                session.user = c_user
                web.seeother("/rooms")
            else:
                return render.intro(self.display, self.message_user_not_found)


class Logout(object):
    def __init__(self):
        pass

    @staticmethod
    def GET():
        if session.logged:
            session.kill()
            web.seeother("/")


class Rooms(object):
    def __init__(self):
        self.rooms = game_lexicon.AssertLexicon()

    def GET(self):
        # If the user called the URL directly, we redirect him
        if session.logged is None:
            web.seeother("/")
        return render.list_rooms(self.rooms.return_rooms(), username=session.user)


class GameEngine(object):
    def __init__(self):
        # We initialize the random images picker
        pic = glob.glob("static/*.jpg")
        random_pic = random.choice(pic)
        self.lexicon = game_lexicon.AssertLexicon()
        # Default view
        self.view = render.show_room(room=session.room, picture=random_pic,
                                     attempts=session.attempts, user=session.user)

    def GET(self):
        # If the user called the URL directly, we redirect him
        if session.user is None:
            web.seeother("/")

        rooms = web.input(room=None)
        get_room = rooms.room
        if get_room:
            if get_room == "Central Corridor":
                session.room = map.central_corridor
            elif get_room == "Laser Weapon Armory":
                session.room = map.laser_weapon_armory
            elif get_room == "The Bridge":
                session.room = map.the_bridge
            elif get_room == "Pod Room":
                session.room = map.pod_room
            elif get_room == "Escape Pod":
                session.room = map.escape_pod
            else:
                session.room = map.central_corridor
            web.seeother("/game")
        else:
            return self.view

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
            session.user = sanitize(user.username)
            web.seeother("/game")

        code = web.input(armory_code=None)
        process = web.input(action=None)
        # We check the parameters
        if process.action:
            if self.lexicon.parse_lexicon(process.action, session.room.name, test=False) is not False:
                session.room = session.room.go(self.lexicon.parse_lexicon(process.action,
                                                                          session.room.name, test=False))
                web.seeother("/game")
            else:
                return render.you_died()
        # View-specific code
        elif code.armory_code:
            if session.attempts != 1:
                if self.lexicon.parse_lexicon(code.armory_code, session.room.name, test=False) is False:
                    session.attempts -= 1
                else:
                    session.room = session.room.go(code.armory_code)
                web.seeother("/game")
            else:
                return render.you_died()
        else:
            return self.view


if __name__ == "__main__":
    app.run()
