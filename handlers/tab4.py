import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab4Handler')
        self.logger.debug('Created Tab4Handler')

        self.app = app

        self.onLambdaPoisson(app.builder.get_object('tab4_spinbutton_poisson'))

    def updateOutSigPlot(self, button):

        self.app.output_signal.cla()

        self.app.fft_output_y = self.app.norm_ampl_fft_fwhl_y * self.app.fft_input_y

        # Using np.abs() method to kill the phase from the FFT
        self.app.output_y = np.abs(np.fft.irfft(self.app.fft_output_y))

        self.app.output_signal.grid(True)
        self.app.output_signal.plot(self.app.non_discrete_input_x, self.app.output_y)

    def onLambdaPoisson(self, lambda_poisson):
        self.app.lambda_value = float(lambda_poisson.get_value())
        self.logger.debug('Current mean value of the Poisson distribution is %s' % self.app.lambda_value)

    def onNoiseCount(self, button):

        # Making noise with Poisson distribution, the mean value
        # is equal to mean_poisson_value
        poisson = np.random.poisson(self.app.lambda_value, self.app.m_value)  # MAKE SOME NO-O-OISE!!!

        self.app.output_signal_with_noise.cla()

        self.app.noise_y = poisson * (self.app.output_y) ** 0.5

        # Summing up the output signal with the noise
        self.app.output_with_noise_y = self.app.output_y + self.app.noise_y

        self.app.output_signal_with_noise.set_xlim(0, self.app.m_value)
        self.app.output_signal_with_noise.set_ylim(0, max(self.app.output_with_noise_y) + 50)
        self.app.output_signal_with_noise.grid(True)
        self.app.output_signal_with_noise.plot(self.app.discrete_input_x, self.app.output_with_noise_y)

        # Calculating the mean value of the noise
        self.app.mean_noise = (sum((self.app.noise_y - np.average(self.app.noise_y)) ** 2) \
                                 /(len(self.app.noise_y)-1)) ** 0.5

        # Calculating the mean value of the signal
        self.app.mean_output_y = sum(self.app.output_y) / len(self.app.non_discrete_input_x)

        # Calculating noise-to-signal ratio
        self.app.noise_to_signal_ratio = self.app.mean_noise / self.app.mean_output_y

        # Updating all calculated values in entries
        # the mean value of the signal
        self.app.mean_noise_entry = self.app.builder.get_object('tab4_entry_mean_signal')
        self.app.mean_noise_entry.set_text(str(self.app.mean_output_y))

        # the mean value of the noise
        self.app.mean_noise_entry = self.app.builder.get_object('tab4_entry_mean_noise')
        self.app.mean_noise_entry.set_text(str(self.app.mean_noise))

        # noise-to-signal ratio
        self.app.noise_to_signal_entry = self.app.builder.get_object('tab4_entry_signal_noise_ratio')
        self.app.noise_to_signal_entry.set_text(str(self.app.noise_to_signal_ratio))

  
