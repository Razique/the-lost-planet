__author__ = 'razique'

import sqlite3
import logging
import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def user_exists(user, passw):
    auth_db = sqlite3.connect(settings.database)
    query = auth_db.execute("SELECT count(*) FROM users where username=? AND password=?", (user, passw))
    (number_of_rows,) = query.fetchone()

    if number_of_rows is 1:
        logging.info("User already exists; skipping... ")
        return False
    else:
        return True


def create_user(user, passw):
    auth_db = sqlite3.connect(settings.database)
    auth_db.execute("INSERT INTO  users(username, password) VALUES (?, ?)", (user, passw))
    try:
        auth_db.commit()
        logging.info("User successfully created.. ")
        return True
    except Warning:
        logging.error("There has been an error, please try again...")
        return False
