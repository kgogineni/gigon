import logging
import bottle

logger = logging.getLogger(__name__)

class ApiServer(object):

    def __init__(self, *args, **kwargs):
        self.app = bottle.app
        self.port = kwargs.get('port')
        self.host = kwargs.get('host')

        if not self.port:
            logger.warn('port is not specified, using the default port.')
            self.port = 8080
        if not self.host:
            logger.warn('hostname is not specified, using the default hostname.')
            self.host = '0.0.0.0'

        self.webroot = 'http://%s:%d/' % (self.host, self.port)

        # we will piggy back on the logger configuration
        self.debug = True if logger.isEnabledFor(logging.DEBUG) else False


    def start(self):
        self.configure(self.webroot)
        bottle.run(self.app, host=self.host, port=self.port, debug=self.debug, server='paste')

    def configure(self, webroot):
        pass

