import hashlib

from django.http import HttpResponse

def password(_password: str):
    pw = _password.strip()
    if len(pw) < 8:
        return HttpResponse("<h1>Password must be atleast 8 characters</h1>")
       
    return hashlib.sha256(pw.encode()).hexdigest()

