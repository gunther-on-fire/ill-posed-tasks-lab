from .tab1 import Handler as Tab1Handler
from .tab2 import Handler as Tab2Handler


class HandlerFinder(object):
    """Searches for handler implementations across multiple objects.
    """
    # See <http://stackoverflow.com/questions/4637792> for why this is
    # necessary.

    def __init__(self, backing_objects):
        self.backing_objects = [Tab1Handler(backing_objects), Tab2Handler(backing_objects)]
    def __getattr__(self, name):
        for o in self.backing_objects:
            if hasattr(o, name):
                return getattr(o, name)
        else:
            raise AttributeError("%r not found on any of %r"
                % (name, self.backing_objects))