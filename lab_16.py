#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

class Tab1Handler:

    def __init__(self, builder):
        self.logger = logging.getLogger('T1Handler')
        self.logger.debug('Created Tab1Handler')

        self.p_value = 2
        self.x_number = None
        self.button = builder.get_object('non-discret-graph')

        self._validate()

    def OnChangedP(self, p):
        self.p_value =  p.get_model()[p.get_active()][0]
        self.logger.debug('New combobox value: %s' % self.p_value)

        self._validate()

    '''
    def ChooseComboBoxValue(self, combobox):
        self.combobox_value =  combobox.get_model()[combobox.get_active()][0]
        self.logger.debug('New combobox value: %s' % self.combobox_value)

        self._validate()
    '''
    def CloseApp(self, *args):
        Gtk.main_quit(*args)

    def XNewValue(self, entry):
        text = entry.get_text()
        self.logger.debug('New X entry value: %s' % text)
        try:
            self.x_number = int(text)
        except:
            self.x_number = None

        self._validate()

    def _validate(self):
        valid = self.p_value is not None and self.x_number is not None
        self.logger.debug("Current state is %s" % ('valid' if valid else 'invalid'))
        self.button.set_sensitive(valid)

logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s] %(message)s', level=logging.DEBUG)
logging.info('Starting application')

logging.debug('Loading UI from glade file')
builder = Gtk.Builder()
builder.add_from_file('lab_step1.glade')

logging.debug('Connecting signals to Tab1Handler')
builder.connect_signals(Tab1Handler(builder))

logging.debug('Showing main window')
window = builder.get_object('Main Window')

logging.debug('Showing non-discrete graph')
non_discrete_graph = builder.get_object('graph before discr')

fig = Figure(dpi=100)
mire_non_discr = fig.add_subplot(111)

p = Tab1Handler(builder)
print(p.p_value)

mire_non_discr_x = np.arange(-10, 10.01, 0.01)
mire_non_discr_y = 0.8*(np.exp(-mire_non_discr_x**p.p_value) + np.exp(-(mire_non_discr_x+3.5)**p.p_value) \
                    + np.exp(-(mire_non_discr_x-3.5)**p.p_value)+ np.exp(-(mire_non_discr_x+7)**p.p_value) \
                    + np.exp(-(mire_non_discr_x-7)**p.p_value))+0.2

mire_non_discr.set_ylim(0.1,1.1)

mire_non_discr.plot(mire_non_discr_x, mire_non_discr_y)

canvas = FigureCanvas(fig)
non_discrete_graph.add_with_viewport(canvas)

window.show_all()

logging.debug('Entering main loop')
Gtk.main()
