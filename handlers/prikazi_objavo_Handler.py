
from google.appengine.api import users, memcache,mail
from handlers.base import BaseHandler
from models.models import Komentar,Objava,Subscriber
from untils.decorator import validate_csrf


class PrikaziObjavoHandler(BaseHandler):
    def get(self, objava_id):
        objava = Objava.get_by_id(int(objava_id))
        seznamkomentarjev = Komentar.query(Komentar.objava_id == str(objava.key.id())).order(Komentar.cas_objave)
        params = {"objava": objava, "seznamkomentarjev": seznamkomentarjev}
        return self.render_template_with_csrf("objave.html", params=params)

    @validate_csrf
    def post(self, objava_id):

        user = users.get_current_user()
        if not user:
            return self.write("Please login before you're allowed to post a topic.")
        vsebina = (self.request.get("komentar"))

        Komentar.shrani_komentar(objava_id,vsebina)

        return self.redirect(objava_id)
class Izbrisi_objavo_Handler(BaseHandler):
    @validate_csrf
    def post(self, objava_id):

        objava = Objava.get_by_id(int(objava_id))
        user = users.get_current_user()

        if objava.uporabnik_email == user.email():
            objava.izbrisano =  True
            objava.put()

        return self.redirect_to("main-page")

class Subscribe_topic_Handler(BaseHandler):

    def post(self, objava_id):
        user = users.get_current_user()
        subscriber = Subscriber(objava_id=objava_id,uporabnik_email=user.email())
        subscriber.put()
        return self.redirect_to("main-page")




