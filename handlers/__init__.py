from .tab1 import Handler as Tab1Handler
from .tab2 import Handler as Tab2Handler
from .tab3 import Handler as Tab3Handler
from .tab4 import Handler as Tab4Handler
from .tab5 import Handler as Tab5Handler
from .tab6 import Handler as Tab6Handler
from .tab7 import Handler as Tab7Handler

class HandlerFinder(object):
    """Searches for handler implementations across multiple objects.
    """
    # See <http://stackoverflow.com/questions/4637792> for why this is
    # necessary.

    def __init__(self, backing_objects):
        self.backing_objects = [Tab1Handler(backing_objects), Tab2Handler(backing_objects),
        Tab3Handler(backing_objects), Tab4Handler(backing_objects), Tab5Handler(backing_objects),
        Tab6Handler(backing_objects), Tab7Handler(backing_objects)]

    def __getattr__(self, name):
        for o in self.backing_objects:
            if hasattr(o, name):
                return getattr(o, name)
        else:
            raise AttributeError("%r not found on any of %r"
                % (name, self.backing_objects))