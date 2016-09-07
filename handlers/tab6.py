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

        self.app.output_signal_with_noise.plot(self.app.discrete_input_x, self.app.output_with_noise_y)


