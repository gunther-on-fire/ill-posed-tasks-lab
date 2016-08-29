import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging
import numpy as np


class Handler:


    def __init__(self, app):
        
        self.logger = logging.getLogger('Tab1Handler')
        self.logger.debug('Created Tab1Handler')
        
        # Attributes of the class
        self.app = app

        # Here we disable plotting because all values will be set only at the end of the next block
        self.do_not_plot = True

        # Populating default values by explicitly calling on-change callbacks
        self.onChangedP(app.builder.get_object('p_parameter_combobox'))
        self.onChangedX(app.builder.get_object('x_length_spin_button'))
        self.onChangedL(app.builder.get_object('l_parameter_list'))
        self.onChangedM(app.builder.get_object('m_parameter_combobox'))

        self.do_not_plot = False

        self.updatePlot()
    
    # Describing the methods of the class
    def onChangedP(self, p):
        
        self.app.p_value =  p.get_model()[p.get_active()][0]
        self.logger.debug('New p value: %s' % self.app.p_value)

        self.updatePlot()

    def onChangedM(self, m):
        
        self.app.m_value =  m.get_model()[m.get_active()][0]
        self.logger.debug('New m value: %s' % self.app.m_value)

        self.updatePlot()

    def onChangedL(self, L):
        
        self.app.L_value = L.get_model()[L.get_active()][0]
        self.logger.debug('New L value: %s' % self.app.L_value)

        self.updatePlot()

    def onChangedX(self, x_length):

        self.app.x_value = int(x_length.get_value())
        self.logger.debug('The highest frequency to cut is f2 = %s' % self.app.x_value)
        
        # x_text_value = entry.get_text()
        # self.logger.debug('New X entry value: %s' % x_text_value)
        # try:
        #     self.app.x_value = int(x_text_value)
        # except:
        #     self.app.x_value = None

        self.updatePlot()

    def closeApp(self, *args):
        Gtk.main_quit(*args)

    def updatePlot(self):

        if self.do_not_plot:
            self.logger.debug('Plotting is currently disabled')
            return

        self.logger.debug('Cleaning plotting area')
        self.app.non_discrete_mire.cla()
        self.app.discrete_mire.cla()

        self.logger.debug('Updating non-discrete plot')

        non_discrete_mire_x = np.linspace(-self.app.x_value/2, self.app.x_value/2, 
            num=self.app.m_value, endpoint=True)
        self.logger.debug('The number of non-discrete plot points is %s' % len(non_discrete_mire_x))

        non_discrete_mire_y = 0.8*(np.e**(-non_discrete_mire_x**self.app.p_value) 
            + np.e**(-(non_discrete_mire_x+3.5)**self.app.p_value)
            + np.e**(-(non_discrete_mire_x-3.5)**self.app.p_value)
            + np.e**(-(non_discrete_mire_x+7)**self.app.p_value)
            + np.e**(-(non_discrete_mire_x-7)**self.app.p_value)) + 0.2
        
        # Setting the limits of the plotting area
        self.app.non_discrete_mire.set_ylim(0.1,1.1)
        self.app.non_discrete_mire.set_xlim(-self.app.x_value/2,self.app.x_value/2)

        # Making the plot
        self.app.non_discrete_mire.plot(non_discrete_mire_x, non_discrete_mire_y)

        self.logger.debug('Updating discrete plot')

        self.app.discrete_mire_x = np.linspace(0, self.app.m_value, self.app.m_value, True)
        self.logger.debug('The number of points is %s' % len(self.app.discrete_mire_x))

        self.app.discrete_mire_y = self.app.L_value*(0.8*(np.e**(-non_discrete_mire_x**self.app.p_value)
            + np.e**(-(non_discrete_mire_x+3.5)**self.app.p_value)
            + np.e**(-(non_discrete_mire_x-3.5)**self.app.p_value)
            + np.e**(-(non_discrete_mire_x+7)**self.app.p_value)
            + np.e**(-(non_discrete_mire_x-7)**self.app.p_value))+0.2)

        self.app.discrete_mire.set_ylim(0, self.app.L_value+50)
        self.app.discrete_mire.set_xlim(0, self.app.m_value)

        self.app.discrete_mire.plot(self.app.discrete_mire_x, self.app.discrete_mire_y, 'o')