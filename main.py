#!/usr/bin/env python

import webapp2
from handlers.dodaj_objavo_Handler import DodajObjavoHandler
from handlers.main_handler import  MainHandler
from handlers.cookie_handler import  CookieHandler
from handlers.prikazi_objavo_Handler import PrikaziObjavoHandler

app = webapp2.WSGIApplication((
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieHandler),
    webapp2.Route('/dodaj-objavo', DodajObjavoHandler),
    webapp2.Route('/prikazi-objavo/<objava_id:\d+>', PrikaziObjavoHandler, name = "objava")


), debug=True)
