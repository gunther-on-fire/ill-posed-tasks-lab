import logging
import numpy as np


class Handler:


    def __init__(self, app):
        self.logger = logging.getLogger('Tab2Handler')
        self.logger.debug('Created Tab2Handler')
        
        self.app = app

    def onDirectFourier(self, button):
        
        self.app.fft_initial.cla()
        
        # Resetting frequency values (see onFrequencyFrom )
        self.app.frequency_from_value = 0
        self.app.frequency_to_value = 0

        # The number of points in fft is half less than
        # the number of points in the input signal because
        # the signal to be transformed is real-valued

        self.app.fft_input_x = np.arange(0, self.app.m_value // 2 + 1)

        self.logger.debug('ω values vector is %s' % len(self.app.fft_input_x))
        self.app.fft_input_y = np.fft.rfft(self.app.discrete_input_y)

        self.app.fft_initial.set_xlim(0, 65)
        self.app.fft_initial.bar(np.arange(len(self.app.fft_input_y)), self.app.fft_input_y,
                                 width=.5, color='b', align='center')
        self.app.fft_initial.grid(True)

    def onCutFrequencies(self, button):

        self.logger.debug('Cleaning plotting area of the FFT of the image')        
        self.app.fft_initial.cla()

        frequency_from = self.app.builder.get_object('tab2_spinbutton_omega_k')
        frequency_to = self.app.builder.get_object('tab2_spinbutton_omega_j')

        self.app.frequency_from_value = int(frequency_from.get_value())
        self.app.frequency_to_value = int(frequency_to.get_value())

        # Setting elements of fft vector from f1 to f2 to 0 
        self.app.fft_input_y[self.app.frequency_from_value:self.app.frequency_to_value + 1] = 0
        self.logger.debug('Cutting frequencies from ' + str(self.app.frequency_from_value) + 'to '
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
        self.app.fft_modified.set_ylim(0, self.app.L_value + 50)
        
        self.app.fft_modified.plot(self.app.discrete_input_x, self.app.inverse_fft_input_y)

        # Calculating information entropy of the modified signal
        self.app.information_entropy_modified = (self.app.m_value
            - (self.app.frequency_to_value - self.app.frequency_from_value)) \
            * np.log2(self.app.L_value)
        
        # Updating the value in the entry
        self.app.information_entropy_modified_entry = self.app.builder.get_object('tab2_entry_information_in')
        self.app.information_entropy_modified_entry.set_text(str(self.app.information_entropy_modified))