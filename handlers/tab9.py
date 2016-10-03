import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab9Handler')
        self.logger.debug('Created Tab9Handler')

        self.app = app

        # Populating default values by explicitly calling on-change callbacks
        self.onChangedAlpha(app.builder.get_object('alpha_spinbutton'))

    def onChangedAlpha(self, alpha):
        
        self.app.alpha = round(float(alpha.get_value()),6)
        self.logger.debug('New alpha value is %s' % self.app.alpha)

    def updateReconstructionPlot(self, button):

        # Clearing the plot area
        self.app.reconstructed_signal.cla()

        self.app.reconstructed_signal.plot(self.app.discrete_input_x, self.app.inverse_fft_input_y)

        self.app.omega = 2*np.pi*self.app.fft_input_x/self.app.x_value

        self.app.reconstructed_input_fft = np.fft.rfft(self.app.output_y + self.app.noise_y)/(self.app.norm_ampl_fft_fwhl_y 
        	+ self.app.alpha*(1+self.app.omega**2)/self.app.norm_ampl_fft_fwhl_y)

        self.app.reconstructed_input_y = np.fft.irfft(self.app.reconstructed_input_fft)

        self.app.reconstructed_signal.set_ylim(0, self.app.L_value + 50)

        self.app.reconstructed_signal.plot(self.app.discrete_input_x, self.app.reconstructed_input_y)
        

        # Calculating the absolute error 
        # sqrt(sum((sig_in-sig_reconstructed)**2)/number_of_counts) -- the standard deviation
        self.app.absolute_error = (sum((self.app.discrete_input_y - self.app.reconstructed_input_y)**2)/len(self.app.discrete_input_x))**0.5

        # Calculating the mean value of the input signal, max/2
        self.app.mean_discrete_input_y = max(self.app.discrete_input_y)/2

        # Calculating the relative error
        self.app.relative_error = (self.app.absolute_error/self.app.mean_discrete_input_y)*100

        self.app.tab_9_store = self.app.builder.get_object('liststoreStep9')

        self.app.tab_9_store.append([self.app.alpha, self.app.absolute_error, self.app.relative_error])
        
