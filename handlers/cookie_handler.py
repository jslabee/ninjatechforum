from handlers.base import BaseHandler
class CookieHandler(BaseHandler):
    def post(self):
        self.response.set_cookie(key="sprejel-piskotek", value="da")
        return self.write("home.html")