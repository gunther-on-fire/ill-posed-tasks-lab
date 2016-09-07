import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab5Handler')
        self.logger.debug('Created Tab5Handler')

        self.app = app

    def updateOutSigPlot(self, button):

        self.app.output_signal.cla()

        self.app.fft_output_y = self.app.norm_ampl_fft_fwhl_y*self.app.fft_input_y

        # Using np.abs() method to kill the phase from the FFT
        self.app.output_y = np.abs(np.fft.irfft(self.app.fft_output_y))

        self.app.output_signal.plot(self.app.non_discrete_input_x, self.app.output_y)