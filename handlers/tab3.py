import logging
import numpy as np


class Handler:


    def __init__(self, app):
        self.logger = logging.getLogger('Tab3Handler')
        self.logger.debug('Created Tab3Handler')

        self.app = app

        # Populating default values by explicitly calling on-change callbacks
        self.onChangedFWHL(app.builder.get_object('fwhl_entry'))

    def onChangedFWHL(self, entry):
        
        fwhl_text_value = entry.get_text()
        self.logger.debug('New FWHL value: %s' % fwhl_text_value)
        try:
            self.app.fwhl_value = int(fwhl_text_value)
        except:
            self.app.fwhl_value = None

    def plotFWHL(self, button):

        non_discrete_fwhl_x = np.linspace(-3, 3, 3/0.01, True)
        self.logger.debug('The number of non-discrete plot points is %s' % len(non_discrete_fwhl_x))
        
        # FWHL=(2/beta)*(ln(2)/pi)**0.5*exp{-(4*ln(2)*x**2/beta**2}

        self.app.non_discrete_fwhl_y = (2/self.app.fwhl_value) \
        *(np.log([2])/np.pi)**0.5*np.e**(-(4*np.log([2]) \
        *non_discrete_fwhl_x**2)/self.app.fwhl_value**2)

        self.app.non_discrete_fwhl.plot(non_discrete_fwhl_x, self.app.non_discrete_fwhl_y)


