import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab5Handler')
        self.logger.debug('Created Tab5Handler')

        self.app = app

    def updateSpectraPlot(self, button):

        self.app.output_and_noise_fft.cla()

        self.app.fft_noise_y = np.abs(np.fft.rfft(self.app.noise_y))
        self.app.ampl_fft_output_y = np.abs(self.app.fft_output_y)

        # Setting plot parameters
        self.app.output_and_noise_fft.set_xlim(-1, int(self.app.builder.get_object('tab5_omega_scale_spinbutton').get_value()))
        self.app.output_and_noise_fft.set_ylim(0, int(self.app.builder.get_object('tab5_signal_scale_spinbutton').get_value()))
        self.app.output_and_noise_fft.set_ylabel('Ф(ω)', fontsize=12)
        self.app.output_and_noise_fft_RIGHT = self.app.output_and_noise_fft.twinx()
        self.app.output_and_noise_fft_RIGHT.set_yticklabels([])
        self.app.output_and_noise_fft_RIGHT.set_ylabel('N(ω)', fontsize=12)

        self.app.output_and_noise_fft.bar(np.arange(len(self.app.fft_input_x)), self.app.ampl_fft_output_y,
                                          width=.5, color='r', align='center')
        self.app.output_and_noise_fft.bar(np.arange(len(self.app.fft_input_x)), self.app.fft_noise_y,
                                          width=.5, color='b', align='center')
        self.app.output_and_noise_fft.legend(["Ф(ω)", "N(ω)"], loc = 2, prop={'size':8})
        self.app.output_and_noise_fft.grid(True)

