import logging

from apiserver import ApiServer
from router import Router

logger = logging.getLogger(__name__)


class GigonServer(ApiServer):
    
    def __init__(self, *args, **kwargs):
        super(GigonServer, self).__init__(*args, **kwargs)



    def configure(self, webroot):
        routes = [
            {
                'url': '/',
                'method': 'GET',
                'invokable' : self.index
            },
            {
                'url': '/',
                'method': 'POST',
                'invokable': self.login
            },
            {
                'url': '/',
                'method': 'POST',
                'invokable': self.register
            },
            {
                'url': '/',
                'method': 'GET',
                'invokable': self.home
            },
        ]
        router = Router()
        router.addRoutes(routes)


    def index(self):
        print('index has been invoked')

    def login(self):
        print('login has been invoked')

    def register(self):
        print('register has been invoked')

    def home(self):
        print('home has been invoked')
