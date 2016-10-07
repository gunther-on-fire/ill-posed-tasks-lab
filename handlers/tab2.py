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

    def onDirectFourier(self, button):

        self.app.fft_initial.cla()

        # The number of points in fft vector is half less than
        # the number of points in discrete mire's one because
        # the function to be transformed is real-valued

        self.app.fft_input_x = np.linspace(0, self.app.m_value//2 + 1, self.app.m_value//2 + 1, True)

        self.logger.debug('ω values vector is %s' % len(self.app.fft_input_x))
        self.app.fft_input_y = np.fft.rfft(self.app.discrete_input_y)

        self.app.fft_initial.set_xlim(0, 65)
        self.app.fft_initial.bar(np.arange(len(self.app.fft_input_y)), self.app.fft_input_y,
                                 width=.5, color='b', align='center')
        self.app.fft_initial.grid(True)

    def onFrequencyFrom(self, frequency_from):

        self.app.frequency_from_value = int(frequency_from.get_value())
        self.logger.debug('The lowest frequency to cut is f1 = %s' % self.app.frequency_from_value)

    def onFrequencyTo(self, frequency_to):

        self.app.frequency_to_value = int(frequency_to.get_value())
        self.logger.debug('The highest frequency to cut is f2 = %s' % self.app.frequency_to_value)

    def onCutFrequencies(self, button):

        self.logger.debug('Cleaning plotting area of the FFT of the image')        
        self.app.fft_initial.cla()

        # Setting elements of fft vector to 0 from f1 to f2
        self.app.fft_input_y[self.app.frequency_from_value:self.app.frequency_to_value + 1] = 0
        self.logger.debug('Cutting frequencies from' + str(self.app.frequency_from_value) + 'to'
                          + str(self.app.frequency_to_value))

        self.app.fft_initial.set_xlim(0, 65)
        self.app.fft_initial.bar(np.arange(len(self.app.fft_input_y)), self.app.fft_input_y,
                                 width=.5, color='b', align='center')
        self.app.fft_initial.grid(True)

    def onInverseFourier(self, button):
        
        self.logger.debug('Cleaning plotting area of the modified image')
        self.app.fft_modified.cla()

        self.logger.debug('X values vector is %s' % len(self.app.fft_input_x))

        # Using np.abs() to kill the phase part of the FFT
        self.app.inverse_fft_input_y = np.abs(np.fft.irfft(self.app.fft_input_y))

        self.app.fft_modified.grid(True)
        self.app.fft_modified.set_xlim(0, self.app.m_value)
        self.app.fft_modified.set_ylim(0, self.app.L_value+50)
        
        self.app.fft_modified.plot(self.app.discrete_input_x, self.app.inverse_fft_input_y)
