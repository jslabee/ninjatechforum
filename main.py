#!/usr/bin/env python

import webapp2

from cron.izbris_cron import Izbristemcron
from handlers.dodaj_objavo_Handler import DodajObjavoHandler
from handlers.main_handler import MainHandler,moji_komentarji_Handler
from handlers.cookie_handler import  CookieHandler
from handlers.prikazi_objavo_Handler import PrikaziObjavoHandler, Izbrisi_objavo_Handler, Subscribe_topic_Handler
from workers.mail_worker import MailWorker
#from.handler import stkomentarjevHandler


app = webapp2.WSGIApplication((
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieHandler),
    webapp2.Route('/dodaj-objavo', DodajObjavoHandler),
    webapp2.Route('/prikazi-objavo/<objava_id:\d+>', PrikaziObjavoHandler),
    webapp2.Route('/task/send-comment-mail',MailWorker),
    webapp2.Route('/prikazi-objavo/<objava_id:\d+>/delete', Izbrisi_objavo_Handler,),
    webapp2.Route('/subscribe/<objava_id:\d+>',Subscribe_topic_Handler),
    webapp2.Route('/mojikomentarji',moji_komentarji_Handler),
    webapp2.Route('/cron/izbris-objav',Izbristemcron)
  #  webapp2.Route('/st-komentarjev<objava_id:\d+>',stkomentarjevHandler)
), debug=True)
