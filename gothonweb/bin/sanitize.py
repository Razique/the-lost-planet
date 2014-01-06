# Takes a input and sanitizes it


def sanitize(cleanme):
    final_string = cleanme[:15]
    return "".join(x for x in final_string if x.isalnum())
