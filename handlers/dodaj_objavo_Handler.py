from google.appengine.api import users
from handlers.base import BaseHandler
from models.models import Objava
from datetime import datetime


class DodajObjavoHandler (BaseHandler):

    def get(self):

        return self.render_template("dodaj-objavo.html")
    def post(self):

        user = users.get_current_user()
        if not user:
            return self.write("Please login before you're allowed to post a topic.")
        naslov = self.request.get("title")
        vsebina = self.request.get("text")

        nova_objava = Objava( naslov = naslov,vsebina = vsebina, uporabnik_email = user.email(),cas_objave = datetime.now() )

        nova_objava.put()
        uri= nova_objava.key.id()

        return self.redirect("prikazi-objavo/"+str(uri))



















