import logging
import numpy as np

class Handler:

    def __init__(self, app):
        self.logger = logging.getLogger('Tab2Handler')
        self.logger.debug('Created Tab2Handler')
        
        self.app = app

        # Populating default values by explicitly calling on-change callbacks
        self.onFrequencyFrom(app.builder.get_object('frequency_from'))
        self.onFrequencyTo(app.builder.get_object('frequency_to'))

    def directFourier(self, button):

        self.logger.debug('X values vector is %s' % len(self.app.discrete_mire_x))
        self.app.fourier_y = np.fft.fft(self.app.discrete_mire_y)
        # The number of points in fft vector is the same with 
        # the number of points in discrete mire's one
        self.app.fft_initial.bar(self.app.discrete_mire_x, self.app.fourier_y, width=.7, color='b')
    
    def onFrequencyFrom(self, frequency_from):

        self.app.frequency_from_value = int(frequency_from.get_value())
        self.logger.debug('The lowest frequency to cut is f1 = %s' % self.app.frequency_from_value)

    def onFrequencyTo(self, frequency_to):

        self.app.frequency_to_value = int(frequency_to.get_value())
        self.logger.debug('The highest frequency to cut is f2 = %s' % self.app.frequency_to_value)

    def cutFrequencies(self, button):

        self.logger.debug('Cleaning plotting area of the FFT of the image')        
        self.app.fft_initial.cla()

        # Setting elements of fft vector to 0 from f1 to f2
        self.app.fourier_y[self.app.frequency_from_value:self.app.frequency_to_value+1] = 0
        self.logger.debug('Cutting frequencies from %s to %s' % (self.app.frequency_from_value,
            self.app.frequency_to_value))

        self.app.fft_initial.bar(self.app.discrete_mire_x, self.app.fourier_y, width=.7, color='b')

    def inverseFourier(self, button):
        
        self.logger.debug('Cleaning plotting area of the modified image')
        self.app.fft_modified.cla()

        self.logger.debug('X values vector is %s' % len(self.app.discrete_mire_x))
        self.app.inverse_fourier_y = np.fft.ifft(self.app.fourier_y)

        self.app.fft_modified.set_ylim(0, self.app.L_value+50)
        self.app.fft_modified.set_xlim(0, self.app.m_value)
        
        self.app.fft_modified.plot(self.app.discrete_mire_x, self.app.inverse_fourier_y)
