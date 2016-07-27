#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

class Tab1Handler:

    def __init__(self, builder, mire_non_discr, mire_discr, fft_before, fft_after):
        self.logger = logging.getLogger('T1Handler')
        self.logger.debug('Created Tab1Handler')

        self.mire_non_discr = mire_non_discr
        self.mire_discr = mire_discr
        self.fft_before = fft_before
        self.fft_after = fft_after

        # Populate default values by explicitly calling on-change callbacks
        # Here we disable plotting because all values will be set only at the end of the next block
        self.do_not_plot = True
        self.On_Changed_P(builder.get_object('p param combobox'))
        self.On_Changed_X(builder.get_object('X length_entry'))
        self.On_Changed_L(builder.get_object('L list'))
        self.On_Changed_M(builder.get_object('m param'))

        self.do_not_plot = False

        self.plot()

    def On_Changed_P(self, p):
        self.p_value =  p.get_model()[p.get_active()][0]
        self.logger.debug('New p value: %s' % self.p_value)

        self.plot()

    def On_Changed_M(self, m):
        self.m_value =  m.get_model()[m.get_active()][0]
        self.logger.debug('New m value: %s' % self.m_value)

        self.plot()

    def On_Changed_L(self, L):
        self.L_value = L.get_model()[L.get_active()][0]
        self.logger.debug('New L value: %s' % self.L_value)

        self.plot()

    def On_Changed_X(self, entry):
        text = entry.get_text()
        self.logger.debug('New X entry value: %s' % text)
        try:
            self.x_number = int(text)
        except:
            self.x_number = None

        self.plot()

    def CloseApp(self, *args):
        Gtk.main_quit(*args)

    def plot(self):

        if self.do_not_plot:
            self.logger.debug('Plotting is currently disabled')
            return

        self.logger.debug('Cleaning plotting area')

        self.mire_non_discr.cla()
        self.mire_discr.cla()

        if self.x_number == None:
            self.mire_non_discr.cla()
            self.mire_discr.cla()
            self.logger.debug('Current state is invalid, not plotting')
            return

        self.logger.debug('Updating non-discrete plot')

        mire_non_discr_x = np.linspace(-self.x_number/2, self.x_number/2, num = self.m_value, endpoint=True)
        self.logger.debug('The number of non-discrete plot points is %s' % len(mire_non_discr_x))
        mire_non_discr_y = 0.8*(np.exp(-mire_non_discr_x**self.p_value) + np.exp(-(mire_non_discr_x+3.5)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-3.5)**self.p_value)+ np.exp(-(mire_non_discr_x+7)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-7)**self.p_value))+0.2
        self.mire_non_discr.set_ylim(0.1,1.1)
        self.mire_non_discr.set_xlim(-self.x_number/2,self.x_number/2)

        self.mire_non_discr.plot(mire_non_discr_x, mire_non_discr_y)

        self.logger.debug('Updating discrete plot')

        mire_discr_x = np.arange(0, self.m_value, 1)
        self.logger.debug('The number of points is %s' % len(mire_discr_x))
        mire_discr_y = self.L_value*(0.8*(np.exp(-mire_non_discr_x**self.p_value) \
                    + np.exp(-(mire_non_discr_x+3.5)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-3.5)**self.p_value)+ np.exp(-(mire_non_discr_x+7)**self.p_value) \
                    + np.exp(-(mire_non_discr_x-7)**self.p_value))+0.2)

        self.mire_discr.set_ylim(0, self.L_value+1)
        self.mire_discr.set_xlim(0,self.m_value)

        self.mire_discr.plot(mire_discr_x, mire_discr_y, 'o')


        fourier_mire_discr_x = np.linspace(0,self.m_value,self.m_value,True)
        self.logger.debug('X values vector is %s' % len(fourier_mire_discr_x))
        fourier_mire_discr_y = np.fft.fft(mire_discr_y)
        self.fft_before.bar(fourier_mire_discr_x, fourier_mire_discr_y, width=.7, color='b')

        fourier_mire_discr_x = np.linspace(0,self.m_value,self.m_value,True)
        self.logger.debug('X values vector is %s' % len(fourier_mire_discr_x))
        fourier_mire_discr_y = np.fft.fft(mire_discr_y)
        self.fft_after.bar(fourier_mire_discr_x, fourier_mire_discr_y, width=.7, color='b')

logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s] %(message)s', level=logging.DEBUG)
logging.info('Starting application')

logging.debug('Loading UI from glade file')
builder = Gtk.Builder()
builder.add_from_file('lab_step1.glade')

logging.debug('Showing main window')
window = builder.get_object('Main Window')

#Tab1

logging.debug('Configuring non-discrete plot')
non_discrete_graph = builder.get_object('graph before discr')

non_discrete_fig = Figure(dpi=100)
mire_non_discr = non_discrete_fig.add_subplot(111)
non_discrete_graph.add_with_viewport(FigureCanvas(non_discrete_fig))

logging.debug('Configuring discrete plot')
discrete_graph = builder.get_object('graph after discr')

discrete_fig = Figure(dpi=100)
mire_discr = discrete_fig.add_subplot(111)
discrete_graph.add_with_viewport(FigureCanvas(discrete_fig))

#Tab2

logging.debug('Calculating FFT of the input data')
fft_before_graph = builder.get_object('Fourier_before')

fft_before_fig = Figure(dpi=100)
fft_before = fft_before_fig.add_subplot(111)
fft_before_graph.add_with_viewport(FigureCanvas(fft_before_fig))

logging.debug('Configuring FFT of the input data')
fft_after_graph = builder.get_object('Fourier_after')

fft_after_fig = Figure(dpi=100)
fft_after = fft_after_fig.add_subplot(111)
fft_after_graph.add_with_viewport(FigureCanvas(fft_after_fig))

logging.debug('Connecting signals to Tab1Handler')
builder.connect_signals(Tab1Handler(builder, mire_non_discr, mire_discr, fft_before, fft_after))

window.show_all()

logging.debug('Entering main loop')
Gtk.main()
