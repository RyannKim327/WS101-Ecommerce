import hashlib, datetime, base64
from django.conf import settings
from django.http import HttpResponse

def encrypt(value):
    return base64.b85encode(value.encode("utf-8")).decode()

def decrypt(value):
    print(value)
    return base64.b85decode(value.encode("utf-8")).decode()

def password(_password: str):
    pw = _password.strip()
    if len(pw) < 8:
        return HttpResponse("<h1>Password must be atleast 8 characters</h1>")
       
    return hashlib.sha256(pw.encode()).hexdigest()

def setCookies(response, key, value):
    try:
        days = 90 * 24 * 60 * 60 * 60
        expires = datetime.datetime.strftime(
            datetime.datetime.utcnow() + datetime.timedelta(seconds=days),
            "%a, %d-%b-%Y %H:%M:%S GMT"
        )
        response.set_cookie(key, encrypt(value), max_age=days, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)
        return {
            "result": True
        }
    except Exception as e:
        return {
            "result": False,
            "message": e
        }
