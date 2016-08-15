import logging
import numpy as np

class Handler:
    def __init__(self, app_state):
        self.logger = logging.getLogger('Tab2Handler')
        self.logger.debug('Created Tab2Handler')

        self.app_state = app_state

    def Fourier_Image(self, button):
        fourier_image_x = np.linspace(0, self.app_state.m_value, self.app_state.m_value, True)
        self.logger.debug('X values vector is %s' % len(fourier_image_x))
        fourier_image_y = np.fft.fft(self.app_state.mire_after_discretization_y)
        self.app_state.fft_before_modification.bar(fourier_image_x, fourier_image_y, width=.7, color='b')

        fourier_image_x = np.linspace(0, self.app_state.m_value, self.app_state.m_value, True)
        self.logger.debug('X values vector is %s' % len(fourier_image_x))
        fourier_image_y = np.fft.fft(self.app_state.mire_after_discretization_y)
        self.app_state.fft_after_modification.bar(fourier_image_x, fourier_image_y, width=.7, color='b')
