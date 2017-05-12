import logging
import bottle

logger = logging.getLogger(__name__)


class Router(object):

    def index(self):
        pass

    def addRoute(self, url, method='GET', invokable=None):

        if not invokable:
            invokable = self.idnex
        bottle.route(url, method, invokable)
        logger.debug('Route \'%s : %s @%s \' has been configured.' % (url, method, invokable))

    def addRoutes(self, routes):
        logger.debug('adding routes..')
        for route in routes:
            logger.debug('processing route %s' % (str(route)))

            self.addRoute(route['url'], route['method'], route['invokable'])

        logger.debug('done adding routes.')