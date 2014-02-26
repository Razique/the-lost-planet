__author__ = 'razique'


def create_user(user, password):
    if user.username:
        # Username init
        session.user = sanitize(user.username)
        web.seeother("/rooms")
    else:
        web.seeother("/")

    if password.password:
        # Password init
        session.password = sanitize(password.password)