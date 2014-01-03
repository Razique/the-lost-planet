# Takes a input and sanitizes it


def sanitize(cleanme):
    return "".join(x for x in cleanme if x.isalnum())
