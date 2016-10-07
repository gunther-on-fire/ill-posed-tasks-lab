import logging
import numpy as np


class Handler:


    def __init__(self, app):
        self.logger = logging.getLogger('Tab3Handler')
        self.logger.debug('Created Tab3Handler')

        self.app = app

        self.do_not_plot = True

        # Populating default values by explicitly calling on-change callbacks
        self.onChangedFWHL(app.builder.get_object('fwhl_value'))
        # self.onWindowChangedFWHL(app.builder.get_object('fwhl_window_spin'))

        self.do_not_plot = False

        self.updateFWHLPlot()

    def onChangedFWHL(self, fwhl):

        self.app.fwhl_value = float(fwhl.get_value())

        self.logger.debug('New FWHL value: %s' % self.app.fwhl_value)

        self.updateFWHLPlot()

    def updateFWHLPlot(self):

        if self.do_not_plot:
            self.logger.debug('Plotting is currently disabled')
            return
        
        self.logger.debug('Cleaning plotting area')
        self.app.non_discrete_fwhl.cla()
        self.app.discrete_fwhl.cla()

        self.logger.debug('Updating non-discrete plot')
        
        # FWHL=(2/beta)*(ln(2)/pi)**0.5*exp{-(4*ln(2)*x**2/beta**2}

        self.app.non_discrete_fwhl_y = (2/self.app.fwhl_value) \
        *(np.log([2])/np.pi)**0.5*np.e**(-(4*np.log([2]) \
        *self.app.non_discrete_input_x**2)/self.app.fwhl_value**2)

        self.app.non_discrete_fwhl.grid(True)
        self.app.non_discrete_fwhl.set_xlim(-10, 10)

        self.app.non_discrete_fwhl.plot(self.app.non_discrete_input_x, self.app.non_discrete_fwhl_y, '^')

        self.app.discrete_fwhl.grid(True)
        self.app.discrete_fwhl.plot(self.app.discrete_input_x, self.app.non_discrete_fwhl_y)




