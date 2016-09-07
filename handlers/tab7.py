import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab7Handler')
        self.logger.debug('Created Tab7Handler')

        self.app = app

    def updateSpectraPlot(self, button):

        self.app.output_and_noise_fft.cla()

        self.app.fft_noise_y = np.abs(np.fft.rfft(self.app.noise_y))
        self.app.ampl_fft_output_y = np.abs(self.app.fft_output_y)

        self.app.output_and_noise_fft.bar(self.app.fft_input_x, self.app.ampl_fft_output_y, width=.7, color='r')
        self.app.output_and_noise_fft.bar(self.app.fft_input_x, self.app.fft_noise_y, width=.7, color='b')                