"""testable python GAE executable"""

# google toolset
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.api import memcache

class MainPage(webapp.RequestHandler):
    def get(self, *args):
        self.response.out.write("This is the main page")
        return
    
class NotFoundPage(webapp.RequestHandler):
    def get(self, *args):
        self.response.out.write("The page you've requested could not be found.")
        return


app = webapp.WSGIApplication([
    ('/', MainPage),
    ('/(.*)', NotFoundPage)
    ], debug = True)


