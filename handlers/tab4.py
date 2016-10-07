import logging
import numpy as np

class Handler:


    def __init__(self, app):

        self.logger = logging.getLogger('Tab4Handler')
        self.logger.debug('Created Tab4Handler')

        self.app = app
    
    def updateFWHLFftPlot(self, button):

        self.app.fft_fwhl.cla()

        # The number of points in fft vector is half less than
        # the number of points in discrete mire's one because
        # the function to be transformed is real-valued

        self.logger.debug('Updating non-discrete plot')
        self.app.fft_fwhl_y = np.fft.rfft(self.app.non_discrete_fwhl_y)
        
        # Correct normalization of the signal, the area under the curve is equal to 1
        # so sum(fhwl_y)*step = 1 => step = 1/sum(fwhl)
        
        self.app.norm_ampl_fft_fwhl_y = np.abs(self.app.fft_fwhl_y) \
        /sum(self.app.non_discrete_fwhl_y)

        self.app.fft_fwhl.set_xlim(0, 65)
        self.app.fft_fwhl.bar(np.arange(len(self.app.fft_input_x)), self.app.norm_ampl_fft_fwhl_y,
                                        width=.5, color='b', align='center')
        self.app.fft_fwhl.grid(True)

  
