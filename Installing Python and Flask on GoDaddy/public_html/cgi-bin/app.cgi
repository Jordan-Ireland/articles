#!/home/USERNAME/.local/bin/python3
import os
import sys
sys.path.insert(0, '/home/USERNAME/public_html/cgi-bin/venv/lib/python3.5/site-packages')
from wsgiref.handlers import CGIHandler
from app import app
class ProxyFix(object):
   def __init__(self, app):
       self.app = app
def __call__(self, environ, start_response):
       environ['SERVER_NAME'] = ""
       environ['SERVER_PORT'] = "80"
       environ['REQUEST_METHOD'] = "GET"
       environ['SCRIPT_NAME'] = ""
       environ['QUERY_STRING'] = ""
       environ['SERVER_PROTOCOL'] = "HTTP/1.1"
       return self.app(environ, start_response)
if __name__ == '__main__':
    app.wsgi_app = ProxyFix(app.wsgi_app)
    CGIHandler().run(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
CGIHandler.run(app)