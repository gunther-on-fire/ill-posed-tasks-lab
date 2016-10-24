import logging
import numpy as np


class Handler:


    def __init__(self, app):
        self.logger = logging.getLogger('Tab3Handler')
        self.logger.debug('Created Tab3Handler')

        self.app = app

    def onChangedFWHL(self, fwhl):

        self.app.fwhl_value = float(fwhl.get_value())

        self.logger.debug('New FWHL value: %s' % self.app.fwhl_value)

        # self.updateFWHLPlot()

    def updateFWHLPlot(self, button):

        self.onChangedFWHL(self.app.builder.get_object('tab3_spinbutton_fwhl'))
        
        self.logger.debug('Cleaning plotting area')
        self.app.non_discrete_fwhl.cla()
        self.app.discrete_fwhl.cla()

        self.logger.debug('Updating non-discrete plot')
        
        # FWHL=(2/beta)*(ln(2)/pi)**0.5*exp{-(4*ln(2)*x**2/beta**2}

        self.app.non_discrete_fwhl_y = (2/self.app.fwhl_value) \
        *(np.log([2])/np.pi)**0.5*np.e**(-(4*np.log([2]) \
        *self.app.non_discrete_input_x**2)/self.app.fwhl_value**2)

        self.app.non_discrete_fwhl.set_xlim(-10, 10)
        self.app.non_discrete_fwhl.set_ylim(0, 1.1 * max(self.app.non_discrete_fwhl_y))
        self.app.non_discrete_fwhl.grid(True)
        self.app.non_discrete_fwhl.plot(self.app.non_discrete_input_x, self.app.non_discrete_fwhl_y)

        self.app.discrete_fwhl.set_xlim(0, len(self.app.discrete_input_x))
        self.app.discrete_fwhl.set_ylim(0, 1.1 * max(self.app.non_discrete_fwhl_y))
        self.app.discrete_fwhl.grid(True)
        self.app.discrete_fwhl.plot(self.app.discrete_input_x, self.app.non_discrete_fwhl_y, 'o')

    def updateFWHLFFTPlot(self, button):

        self.app.fft_fwhl.cla()

        # The number of points in fft vector is half less than
        # the number of points in discrete mire's one because
        # the function to be transformed is real-valued

        self.logger.debug('Updating non-discrete plot')
        self.app.fft_fwhl_y = np.fft.rfft(self.app.non_discrete_fwhl_y)

        # Correct normalization of the signal, the area under the curve is equal to 1
        # so sum(fhwl_y)*step = 1 => step = 1/sum(fwhl)

        self.app.norm_ampl_fft_fwhl_y = np.abs(self.app.fft_fwhl_y) \
                                        / sum(self.app.non_discrete_fwhl_y)

        self.app.fft_fwhl.set_xlim(-1, 65)
        self.app.fft_fwhl.bar(np.arange(len(self.app.fft_input_x)), self.app.norm_ampl_fft_fwhl_y,
                              width=.5, color='b', align='center')
        self.app.fft_fwhl.grid(True)




