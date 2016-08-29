import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab4Handler')
        self.logger.debug('Created Tab4Handler')

        self.app = app

        self.plotFWHLFourier()
    
    def plotFWHLFourier(self):

        self.logger.debug('Updating non-discrete plot')
        self.app.fwhl_fourier_y = np.fft.fft(self.app.non_discrete_fwhl_y)
        self.app.fwhl_fourier.bar(self.app.discrete_mire_x, self.app.fwhl_fourier_y, width=.7, color='b')


  
