from handlers.base import BaseHandler
from google.appengine.api import users, memcache,mail

class MailWorker(BaseHandler):
    def post(self):
        emailavtorjaobjave=self.request.get("email_avtorja_objave")
        emailavtorjakomentarja = self.request.get("email_avtorja_komentarja")
        mail.send_mail(sender="jslabe@gmail.com",
                       to= emailavtorjaobjave,
                       subject="prisel je nov komentar",
                       body ="<b>%s<b>je v tvoji temi napisal nov komentar" % emailavtorjakomentarja)

class MailWorkersubscribers(BaseHandler):
    def post(self):
        subscriberemail =self.request.get("subscriberemail")
        emailavtorjakomentarja = self.request.get("email_avtorja_komentarja")
        mail.send_mail(sender="jslabe@gmail.com",
                       to= subscriberemail,
                       subject="prisel je nov komentar",
                       body ="<b>%s<b>je v tvoji temi napisal nov komentar" % emailavtorjakomentarja)

