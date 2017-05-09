# -*- coding: utf-8 -*-
import logging

#import bottle

logger = logging.getLogger(__name__)

class Gigon(object):
    def __init__(self):
        print('Initializing the Caster...')
        if logger.isEnabledFor(logging.DEBUG):
            self.debug = True
        else:
            self.debug = False

        self.__init_bottle()
        pass

    def __init_bottle(self):
        #self.app = bottle.app()
        self.port = 8080
        self.host = 'localhost'
        self.webroot = 'http://%s:%d/' % (self.host, self.port)

    def start(self):
        print('Starting the Caster...!')
        self.setup_routes()
        #bottle.run(self.app, host=self.host, port=self.port, debug=self.debug, server='paste')

    def setup_routes(self):
        pass

        #rt_manager = RouteManager()
        # get requests
        #rt_manager.addRoute('/', 'GET', rt_manager.getIndex)
        #rt_manager.addRoute('/caster', 'GET', rt_manager.getIndex)
        # rt_manager.addRoute('/meds', 'GET', MedsList().listmeds)

