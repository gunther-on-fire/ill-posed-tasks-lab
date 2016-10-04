import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab5Handler')
        self.logger.debug('Created Tab5Handler')

        self.app = app

    def updateOutSigPlot(self, button):

        self.app.output_signal.cla()
        self.app.noise_to_signal_entry = self.app.builder.get_object('signal_noise_ratio_entry')
        self.app.noise_to_signal_entry.set_text('0')  

        self.app.fft_output_y = self.app.norm_ampl_fft_fwhl_y*self.app.fft_input_y

        # Using np.abs() method to kill the phase from the FFT
        self.app.output_y = np.abs(np.fft.irfft(self.app.fft_output_y))

        self.app.output_signal.plot(self.app.non_discrete_input_x, self.app.output_y)

        # Calculating noise/signal ratio

        self.app.mean_output_y = sum(self.app.output_y)/len(self.app.non_discrete_input_x)
        
        self.app.mean_noise = self.app.builder.get_object('mean_poisson')
        self.app.noise_to_signal_ratio = self.app.mean_output_y/float(self.app.mean_noise.get_value())
        

        #TOFIX: Entry update doesn't work
        self.app.noise_to_signal_entry = self.app.builder.get_object('signal_noise_ratio_entry')
        self.app.noise_to_signal_entry.set_text(str(self.app.noise_to_signal_ratio))