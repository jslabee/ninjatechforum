from handlers.base import BaseHandler
from models.models import Objava

class MainHandler(BaseHandler):
    def get(self):
        seznamobjav = Objava.query().fetch()
        params = {"seznamobjav": seznamobjav}
        return self.render_template("home.html", params=params)
