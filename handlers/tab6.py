import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab6Handler')
        self.logger.debug('Created Tab6Handler')

        self.app = app

        self.onLambdaPoisson(app.builder.get_object('mean_poisson'))

    def onLambdaPoisson(self, lambda_poisson):

        self.app.lambda_value = float(lambda_poisson.get_value())
        self.logger.debug('Current mean value of the Poisson distribution is %s' % self.app.lambda_value)

    def onNoiseCount(self, button):

        # Making noise with Poisson distribution, the mean value
        # is equal to mean_poisson_value
        poisson = np.random.poisson(self.app.lambda_value, self.app.m_value) # MAKE SOME NO-O-OISE!!!

        self.app.output_signal_with_noise.cla()    	

        self.app.noise_y = poisson*(self.app.output_y)**0.5


        # Summing up the output signal with the noise 
        self.app.output_with_noise_y = self.app.output_y + self.app.noise_y

        self.app.output_signal_with_noise.set_xlim(0, self.app.m_value)
        self.app.output_signal_with_noise.grid(True)
        self.app.output_signal_with_noise.plot(self.app.discrete_input_x, self.app.output_with_noise_y)

        # Calculating noise/signal ratio

        self.app.mean_output_y = sum(self.app.output_y)/len(self.app.non_discrete_input_x)
        
        self.app.mean_noise = self.app.builder.get_object('mean_poisson')
        self.app.noise_to_signal_ratio = self.app.mean_output_y/float(self.app.mean_noise.get_value())
        

        # Update noise-to-signal ratio entry
        self.app.noise_to_signal_entry = self.app.builder.get_object('signal_noise_ratio_entry')
        self.app.noise_to_signal_entry.set_text(str(self.app.noise_to_signal_ratio))


