# -*- coding: utf-8 -*-
import logging
from server import GigonServer

#import bottle

logger = logging.getLogger(__name__)

class Gigon(object):
    def __init__(self):
        print('Initializing the Caster...')

        # we will piggy back on the logger configuration
        self.debug = True if logger.isEnabledFor(logging.DEBUG) else False
        self.server = GigonServer()


    def bootstrap(self):
        self.server.start()  # start the api server


if __name__ == '__main__':
    gigon = Gigon()
    gigon.bootstrap()
