from handlers.base import BaseHandler
from models.models import Objava
from models.models import Komentar
from google.appengine.api import users

class MainHandler(BaseHandler):
    def get(self):
        seznamobjav = Objava.query(Objava.izbrisano == False).order(Objava.cas_objave).fetch()
        seznamkomentarjev = Komentar.query().fetch()
        params = {"seznamkomentarjev": seznamkomentarjev,"seznamobjav": seznamobjav}
        return self.render_template("home.html", params=params)

class moji_komentarji_Handler(BaseHandler):
    def get (self):
        user = users.get_current_user()
        kometarji = Komentar.query(Komentar.uporabnik_email == user.email()).fetch()
        params = {"komentarji":kometarji}
        return self.render_template("mojeobjave.html",params=params)


