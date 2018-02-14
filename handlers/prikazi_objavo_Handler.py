
from handlers.base import BaseHandler
from models.models import Objava

class PrikaziObjavoHandler(BaseHandler):
    def get(self, objava_id):
        objava = Objava.get_by_id(int(objava_id))
        params = {"objava": objava}
        return self.render_template("objave.html", params=params)



