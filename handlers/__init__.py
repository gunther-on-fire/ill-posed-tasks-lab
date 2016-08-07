from .tab1 import Handler as Tab1Handler
from .tab2 import Handler as Tab2Handler


class HandlerFinder(object):
    """Searches for handler implementations across multiple objects.
    """
    # See <http://stackoverflow.com/questions/4637792> for why this is
    # necessary.

    def __init__(self, app_state):
        self.backing_objects = [Tab1Handler(app_state), Tab2Handler(app_state)]

    def __getattr__(self, name):
        for o in self.backing_objects:
            if hasattr(o, name):
                return getattr(o, name)
        else:
            raise AttributeError("%r not found on any of %r"
                % (name, self.backing_objects))
