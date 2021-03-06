from logging.config import fileConfig
import os.path
fileConfig(r'/usr/local/mapproxy/log.ini', {'here': os.path.dirname(__file__)})

from mapproxy.wsgiapp import make_wsgi_app
application = make_wsgi_app(r'/usr/local/mapproxy/mapproxy.yaml')