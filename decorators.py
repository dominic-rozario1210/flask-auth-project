from flask import session,redirect

from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        if "user" not in session:
            return redirect("/login")
        return func(*args,**kwargs)
    return wrapper