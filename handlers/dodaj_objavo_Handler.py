import uuid

from google.appengine.api import users, memcache
from handlers.base import BaseHandler
from models.models import Objava
from datetime import datetime
import cgi
import uuid


class DodajObjavoHandler (BaseHandler):

    def get(self):

        csrf_token = str(uuid.uuid4())  # convert UUID to string
        memcache.add(key=csrf_token, value=True, time=600)

        params = {"csrf_token": csrf_token}

        return self.render_template("dodaj-objavo.html", params=params)
    def post(self):
        csrf_token = self.request.get("csrf_token")
        mem_token = memcache.get(key=csrf_token)  # find if this CSRF exists in memcache

        if not mem_token:  # if token does not exist in memcache, write the following message
            return self.write("You are evil attacker...")

        user = users.get_current_user()
        if not user:
            return self.write("Please login before you're allowed to post a topic.")
        naslov = cgi.escape(self.request.get("title"))
        vsebina = cgi.escape(self.request.get("text"))

        nova_objava = Objava( naslov = naslov,vsebina = vsebina, uporabnik_email = user.email(),cas_objave = datetime.now() )

        nova_objava.put()
        uri= nova_objava.key.id()

        return self.redirect("prikazi-objavo/"+str(uri))



















