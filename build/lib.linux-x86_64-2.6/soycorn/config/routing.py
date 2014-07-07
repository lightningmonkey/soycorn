"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('home', '/', controller='news', action='index', title='index')
    map.connect('home', '/index', controller='news', action='index', title='index')
    map.connect('article', '/news/{title}', controller='news', action='article')
    map.connect('newshome', '/News', controller='news', action='news')
    map.connect('photo', '/Photo-Gallery/{title}', controller='news', action='photo')
    

    map.connect('/{title}', controller='news', action='show')
    
    return map

