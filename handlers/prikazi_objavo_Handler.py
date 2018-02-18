import uuid

from google.appengine.api import users, memcache
from handlers.base import BaseHandler
from models.models import Komentar
from datetime import datetime
import cgi
from models.models import Objava
import uuid


class PrikaziObjavoHandler(BaseHandler):
    def get(self, objava_id):
        csrf_token = str(uuid.uuid4())  # convert UUID to string
        memcache.add(key=csrf_token, value=True, time=600)
        objava = Objava.get_by_id(int(objava_id))
        seznamkomentarjev = Komentar.query(Komentar.objava_id == str(objava.key.id())).order(Komentar.cas_objave)
        params = {"objava": objava, "seznamkomentarjev": seznamkomentarjev,"csrf_token": csrf_token}
        return self.render_template("objave.html", params=params)



    def post(self, objava_id):
        csrf_token = self.request.get("csrf_token")
        mem_token = memcache.get(key=csrf_token)  # find if this CSRF exists in memcache

        if not mem_token:  # if token does not exist in memcache, write the following message
            return self.write("You are evil attacker...")

        user = users.get_current_user()
        if not user:
            return self.write("Please login before you're allowed to post a topic.")
        vsebina = cgi.escape(self.request.get("komentar"))

        nov_kometar = Komentar(objava_id=objava_id, vsebina=vsebina, uporabnik_email=user.email(), cas_objave=datetime.now())
        nov_kometar.put()
        return self.redirect(objava_id)













