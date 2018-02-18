from handlers.base import BaseHandler
from models.models import Objava
from models.models import Komentar

class MainHandler(BaseHandler):
    def get(self):
        seznamobjav = Objava.query().order(Objava.cas_objave).fetch()
        seznamkomentarjev = Komentar.query().fetch()
        params = {"seznamkomentarjev": seznamkomentarjev,"seznamobjav": seznamobjav}
        return self.render_template("home.html", params=params)


