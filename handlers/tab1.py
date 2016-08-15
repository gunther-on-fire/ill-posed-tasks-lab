import logging
import numpy as np

from gi.repository import Gtk

class Handler:

    def __init__(self, app_state):
        self.logger = logging.getLogger('Tab1Handler')
        self.logger.debug('Created Tab1Handler')

        self.app_state = app_state

        # Populate default values by explicitly calling on-change callbacks
        # Here we disable plotting because all values will be set only at the end of the next block
        self.do_not_plot = True
        self.On_Changed_P(self.app_state.builder.get_object('p_parameter_combobox'))
        self.On_Changed_X(self.app_state.builder.get_object('x_length_entry'))
        self.On_Changed_L(self.app_state.builder.get_object('l_parameter_list'))
        self.On_Changed_M(self.app_state.builder.get_object('m_parameter_combobox'))

        self.do_not_plot = False

        self.plot()

    def On_Changed_P(self, p):
        self.app_state.p_value =  p.get_model()[p.get_active()][0]
        self.logger.debug('New p value: %s' % self.app_state.p_value)

        self.plot()

    def On_Changed_M(self, m):
        self.app_state.m_value =  m.get_model()[m.get_active()][0]
        self.logger.debug('New m value: %s' % self.app_state.m_value)

        self.plot()

    def On_Changed_L(self, L):
        self.app_state.L_value = L.get_model()[L.get_active()][0]
        self.logger.debug('New L value: %s' % self.app_state.L_value)

        self.plot()

    def On_Changed_X(self, entry):
        text = entry.get_text()
        self.logger.debug('New X entry value: %s' % text)
        try:
            self.app_state.x_number = int(text)
        except:
            self.app_state.x_number = None

        self.plot()

    def CloseApp(self, *args):
        Gtk.main_quit(*args)

    def plot(self):

        if self.do_not_plot:
            self.logger.debug('Plotting is currently disabled')
            return

        self.logger.debug('Cleaning plotting area')

        self.app_state.mire_before_discretization.cla()
        self.app_state.mire_after_discretization.cla()

        if self.app_state.x_number == None:
            self.app_state.mire_before_discretization.cla()
            self.app_state.mire_after_discretization.cla()
            self.logger.debug('Current state is invalid, not plotting')
            return

        self.logger.debug('Updating non-discrete plot')

        mire_before_discretization_x = np.linspace(-self.app_state.x_number/2, self.app_state.x_number/2, num = self.app_state.m_value, endpoint=True)
        self.logger.debug('The number of non-discrete plot points is %s' % len(mire_before_discretization_x))
        mire_before_discretization_y = 0.8*(np.exp(-mire_before_discretization_x**self.app_state.p_value) + np.exp(-(mire_before_discretization_x+3.5)**self.app_state.p_value) \
                    + np.exp(-(mire_before_discretization_x-3.5)**self.app_state.p_value)+ np.exp(-(mire_before_discretization_x+7)**self.app_state.p_value) \
                    + np.exp(-(mire_before_discretization_x-7)**self.app_state.p_value))+0.2
        self.app_state.mire_before_discretization.set_ylim(0.1,1.1)
        self.app_state.mire_before_discretization.set_xlim(-self.app_state.x_number/2,self.app_state.x_number/2)

        self.app_state.mire_before_discretization.plot(mire_before_discretization_x, mire_before_discretization_y)

        self.logger.debug('Updating discrete plot')

        mire_after_discretization_x = np.arange(0, self.app_state.m_value, 1)
        self.logger.debug('The number of points is %s' % len(mire_after_discretization_x))
        self.app_state.mire_after_discretization_y = self.app_state.L_value*(0.8*(np.exp(-mire_before_discretization_x**self.app_state.p_value) \
                    + np.exp(-(mire_before_discretization_x+3.5)**self.app_state.p_value) \
                    + np.exp(-(mire_before_discretization_x-3.5)**self.app_state.p_value)+ np.exp(-(mire_before_discretization_x+7)**self.app_state.p_value) \
                    + np.exp(-(mire_before_discretization_x-7)**self.app_state.p_value))+0.2)

        self.app_state.mire_after_discretization.set_ylim(0, self.app_state.L_value+1)
        self.app_state.mire_after_discretization.set_xlim(0,self.app_state.m_value)

        self.app_state.mire_after_discretization.plot(mire_after_discretization_x, self.app_state.mire_after_discretization_y, 'o')
