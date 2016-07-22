#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

class Tab1Handler:

    def __init__(self, builder, mire_non_discr, mire_discr):
        self.logger = logging.getLogger('T1Handler')
        self.logger.debug('Created Tab1Handler')

        self.mire_non_discr = mire_non_discr
        self.mire_discr = mire_discr

        # Populate default values by explicitly calling on-change callbacks
        # Here we disable plotting because all values will be set only at the end of the next block
        self.do_not_plot = True
        self.OnChangedP(builder.get_object('p param combobox'))
        self.XNewValue(builder.get_object('X length_entry'))
        self.OnChangedL(builder.get_object('L list'))
        self.OnChangedM(builder.get_object('m param'))

        self.do_not_plot = False

        self.plot()

    def OnChangedP(self, p):
        self.p_value =  p.get_model()[p.get_active()][0]
        self.logger.debug('New p value: %s' % self.p_value)

        self.plot()

    def OnChangedM(self, m):
        self.m_value =  m.get_model()[m.get_active()][0]
        self.logger.debug('New m value: %s' % self.m_value)

        self.plot()


    def OnChangedL(self, L):
        self.L_value = L.get_model()[L.get_active()][0]
        self.logger.debug('New L value: %s' % self.L_value)

        self.plot()

    def CloseApp(self, *args):
        Gtk.main_quit(*args)

    def XNewValue(self, entry):
        text = entry.get_text()
        self.logger.debug('New X entry value: %s' % text)
        try:
            self.x_number = int(text)
        except:
            self.x_number = None

        self.plot()

    def plot(self):

        if self.do_not_plot:
            self.logger.debug('Plotting is currently disabled')
            return

        self.logger.debug('Cleaning plotting area')

        self.mire_non_discr.cla()
        self.mire_discr.cla()

        if not all([self.x_number, self.m_value, self.p_value, self.L_value]):
            self.logger.debug('Current state is invalid, not plotting')
            return

        self.logger.debug('Updating non-discrete plot')

        mire_non_discr_x = np.arange(-self.x_number/2, self.x_number/2+0.01, self.x_number/(self.m_value-1))
        mire_non_discr_y = 0.8*(np.exp(-mire_non_discr_x**self.p_value) + np.exp(-(mire_non_discr_x+3.5)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-3.5)**self.p_value)+ np.exp(-(mire_non_discr_x+7)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-7)**self.p_value))+0.2
        self.mire_non_discr.set_ylim(0.1,1.1)
        self.mire_non_discr.set_xlim(-self.x_number/2,self.x_number/2)

        self.mire_non_discr.plot(mire_non_discr_x, mire_non_discr_y)

        self.logger.debug('Updating discrete plot')

        mire_discr_x = np.arange(0, self.m_value, 1)
        mire_non_discr_x = np.arange(-self.x_number/2, self.x_number/2+0.01, self.x_number/(self.m_value-1))

        mire_discr_y = self.L_value*(0.8*(np.exp(-mire_non_discr_x**self.p_value) \
                    + np.exp(-(mire_non_discr_x+3.5)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-3.5)**self.p_value)+ np.exp(-(mire_non_discr_x+7)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-7)**self.p_value))+0.2)

        self.mire_discr.set_ylim(0, self.L_value+1)
        self.mire_discr.set_xlim(0,self.m_value)

        self.mire_discr.plot(mire_discr_x, mire_discr_y, 'o')

logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s] %(message)s', level=logging.DEBUG)
logging.info('Starting application')

logging.debug('Loading UI from glade file')
builder = Gtk.Builder()
builder.add_from_file('lab_step1.glade')

logging.debug('Showing main window')
window = builder.get_object('Main Window')

logging.debug('Configuring non-discrete plot')
non_discrete_graph = builder.get_object('graph before discr')

fig = Figure(dpi=100)
mire_non_discr = fig.add_subplot(111)
non_discrete_graph.add_with_viewport(FigureCanvas(fig))

logging.debug('Configuring discrete plot')
discrete_graph = builder.get_object('graph after discr')

fig2 = Figure(dpi=100)
mire_discr = fig2.add_subplot(111)
discrete_graph.add_with_viewport(FigureCanvas(fig2))

logging.debug('Connecting signals to Tab1Handler')
builder.connect_signals(Tab1Handler(builder, mire_non_discr, mire_discr))

window.show_all()

logging.debug('Entering main loop')
Gtk.main()
