from google.appengine.ext import ndb
from google.appengine.api import users, memcache,taskqueue

class Subscriber(ndb.Model):
    objava_id = ndb.StringProperty()
    uporabnik_email = ndb.StringProperty()

class Objava(ndb.Model):
    vsebina = ndb.TextProperty()
    naslov = ndb.StringProperty()
    uporabnik_email =ndb.StringProperty()
    cas_objave = ndb.DateTimeProperty()
    cas_posodobitve = ndb.DateTimeProperty()
    izbrisano = ndb.BooleanProperty(default=False)
    cas_izbrisa = ndb.DateTimeProperty()

class Komentar(ndb.Model):
    objava_id = ndb.StringProperty()
    vsebina = ndb.TextProperty()
    naslov_objave = ndb.TextProperty()
    uporabnik_email = ndb.StringProperty()
    cas_objave = ndb.DateTimeProperty()
    cas_posodobitve = ndb.DateTimeProperty()
    izbrisano = ndb.BooleanProperty(default=False)
    cas_izbrisa = ndb.DateTimeProperty()

    @staticmethod
    def shrani_komentar(objava_id,vsebina):
        uporabnik = users.get_current_user()
        email = uporabnik.email()
        objava = Objava.get_by_id(int(objava_id))
        naslov = objava.naslov
        subscriber = Subscriber.uporabnik_email

        nov_komentar = Komentar(vsebina=vsebina,
                                uporabnik_email=email,
                                objava_id=objava_id,
                                naslov_objave= naslov)
        nov_komentar.put()


        taskqueue.add(url='/task/send-comment-mail',
                      params={
                          "subscriberemail":subscriber,
                          "email_avtorja_objave":objava.uporabnik_email,
                          "email_avtorja_komentarja":email
                      })

