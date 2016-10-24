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
        self.onChangedP(app.builder.get_object('tab1_combobox_p'))
        self.onChangedX(app.builder.get_object('tab1_spinbutton_x'))
        self.onChangedL(app.builder.get_object('tab1_combobox_l'))
        self.onChangedM(app.builder.get_object('tab1_combobox_m'))

        self.do_not_plot = False

        self.updateInSigPlot()

    # Describing the methods of the class
    def onChangedP(self, p):
        self.app.p_value = p.get_model()[p.get_active()][0]
        self.logger.debug('New p value: %s' % self.app.p_value)

        self.updateInSigPlot()

    def onChangedM(self, m):
        self.app.m_value = m.get_model()[m.get_active()][0]
        self.logger.debug('New m value: %s' % self.app.m_value)

        self.updateInSigPlot()

    def onChangedL(self, L):
        self.app.L_value = L.get_model()[L.get_active()][0]
        self.logger.debug('New L value: %s' % self.app.L_value)

        self.updateInSigPlot()

    def onChangedX(self, x_length):
        self.app.x_value = int(x_length.get_value())
        self.logger.debug('New X value is %s' % self.app.x_value)

        self.updateInSigPlot()

    def closeApp(self, *args):
        Gtk.main_quit(*args)

    def updateInSigPlot(self):
        if self.do_not_plot:
            self.logger.debug('Plotting is currently disabled')
            return

        self.logger.debug('Cleaning plotting area')
        self.app.non_discrete_input.cla()
        self.app.discrete_input.cla()

        self.logger.debug('Updating non-discrete plot')

        self.app.non_discrete_input_x = np.linspace(-self.app.x_value / 2, self.app.x_value / 2,
                                                    num=self.app.m_value, endpoint=True)
        self.logger.debug('The number of non-discrete plot points is %s'
                          % len(self.app.non_discrete_input_x))

        non_discrete_input_y = 0.8 * (np.e ** (-self.app.non_discrete_input_x ** self.app.p_value)
                                      + np.e ** (-(self.app.non_discrete_input_x + 3.5) ** self.app.p_value)
                                      + np.e ** (-(self.app.non_discrete_input_x - 3.5) ** self.app.p_value)
                                      + np.e ** (-(self.app.non_discrete_input_x + 7) ** self.app.p_value)
                                      + np.e ** (-(self.app.non_discrete_input_x - 7) ** self.app.p_value)) + 0.2

        # Setting the limits of the plotting area
        self.app.non_discrete_input.set_ylim(0.1, 1.1)
        self.app.non_discrete_input.set_xlim(-self.app.x_value / 2, self.app.x_value / 2)
        self.app.non_discrete_input.grid(True)

        # Making the plot
        self.app.non_discrete_input.plot(self.app.non_discrete_input_x, non_discrete_input_y)

        self.logger.debug('Updating discrete plot')

        self.app.discrete_input_x = np.linspace(0, self.app.m_value, self.app.m_value, True)
        self.logger.debug('The number of points is %s' % len(self.app.discrete_input_x))

        self.app.discrete_input_y = self.app.L_value \
                                    * (0.8 * (np.e ** (-self.app.non_discrete_input_x ** self.app.p_value)
                                              + np.e ** (-(self.app.non_discrete_input_x + 3.5) ** self.app.p_value)
                                              + np.e ** (-(self.app.non_discrete_input_x - 3.5) ** self.app.p_value)
                                              + np.e ** (-(self.app.non_discrete_input_x + 7) ** self.app.p_value)
                                              + np.e ** (-(self.app.non_discrete_input_x - 7) ** self.app.p_value))
                                              + 0.2)

        self.app.discrete_input.set_ylim(0, 1.1 * self.app.L_value)
        self.app.discrete_input.set_xlim(0, self.app.m_value)
        self.app.discrete_input.grid(True)

        self.app.discrete_input.plot(self.app.discrete_input_x, self.app.discrete_input_y, 'o')

        # Calculating information entropy
        self.app.information_entropy = self.app.m_value * np.log2(self.app.L_value)

        # Updating the value in information entropy entry
        self.app.information_entropy_entry = self.app.builder.get_object('tab1_entry1')
        self.app.information_entropy_entry.set_text(str(self.app.information_entropy))