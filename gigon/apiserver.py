import logging
import bottle

logger = logging.getLogger(__name__)

class ApiServer(object):

    def __init__(self, *args, **kwargs):
        self.app = bottle.app
        self.port = kwargs['port']
        self.host = kwargs['host']

        if not self.port:
            logger.warn('port is not specified, using the default port.')
            self.port = 8080
        if not self.host:
            logger.warn('hostname is not specified, using the default hostname.')
            self.host = 'localhost'

        self.webroot = 'http://%s:%d/' % (self.port, self.host)

        # we will piggy back on the logger configuration
        self.debug = True if logger.isEnabledFor(logging.DEBUG) else False


    def start(self):
        self.configure(self.webroot)
        bottle.run(self.app, host=self.host, port=self.port, debug=self.debug, server='paste')

    def configure(self, webroot):
        pass

