import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab6Handler')
        self.logger.debug('Created Tab6Handler')

        self.app = app

    def onCalculateParameters(self, button):

        # Getting the value of max frequency
        self.app.max_frequency = self.app.builder.get_object('tab6_spinbutton_omega_max')
        self.app.max_frequency_value = int(self.app.max_frequency.get_value())

        # Calculating the value of Q function
        self.app.q_function = round(1 - (1.047 - 1.286 / (1 / self.app.noise_to_signal_ratio)) \
        / np.log2(1 / self.app.noise_to_signal_ratio), 2)

        # Calculating the value of Shannon's K coefficient
        self.app.shannon_coefficient = \
        round(np.e ** (sum(np.log(self.app.norm_ampl_fft_fwhl_y[:self.app.max_frequency_value + 1])) \
                                     /(2*np.pi * self.app.max_frequency_value)), 2)

        # Calculating the value of the min error
        self.app.min_error = round(self.app.noise_to_signal_ratio / self.app.shannon_coefficient, 2)

        # Updating all calculated values in entries
        # S/N parameter
        self.app.signal_to_noise_entry = self.app.builder.get_object('tab6_entry_signal_noise_ratio')
        self.app.signal_to_noise_entry.set_text(str(1 / self.app.noise_to_signal_ratio))

        # Q function
        self.app.q_function_entry = self.app.builder.get_object('tab6_entry_Q')
        self.app.q_function_entry.set_text(str(self.app.q_function))

        # Shannon's K coefficient
        self.app.shannon_coefficient_entry = self.app.builder.get_object('tab6_entry_K')
        self.app.shannon_coefficient_entry.set_text(str(self.app.shannon_coefficient))

        # minimal error
        self.app.min_error_entry = self.app.builder.get_object('tab6_entry_min_error')
        self.app.min_error_entry.set_text(str(self.app.min_error))

        # Calculating information entropy of the reconstructed signal
        self.app.information_entropy_reconstructed = 2 * np.pi * self.app.max_frequency_value * self.app.q_function \
        * np.log2(1 / self.app.noise_to_signal_ratio) * self.app.shannon_coefficient

        # Updating the value in the entry
        self.app.information_entropy_reconstructed_entry = self.app.builder.get_object('tab6_entry_information_out')
        self.app.information_entropy_reconstructed_entry.set_text(str(self.app.information_entropy_reconstructed))