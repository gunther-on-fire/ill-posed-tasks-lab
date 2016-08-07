#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

import handlers


class ApplicationState:

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)


#Check Frequency_Cut function, it doesn't work

    # def Frequency_Cut(self, entry_start, entry_end):
    #     frequency_start = entry_start.get_text()
    #     frequency_end = entry_end.get.get_text()
    #     self.logger.debug('Cutting frequencies from %s to %s' % frequency_start % frequency_end)



logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s] %(message)s', level=logging.DEBUG)
logging.info('Starting application')

logging.debug('Loading UI from glade file')
builder = Gtk.Builder()
builder.add_from_file('lab_step1.glade')

logging.debug('Showing main window')
window = builder.get_object('Main Window')

app_state = ApplicationState()

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

logging.debug('Connecting signals')
app_state.builder = builder
app_state.mire_non_discr = mire_non_discr
app_state.mire_discr = mire_discr
app_state.fft_before = fft_before
app_state.fft_after = fft_after

builder.connect_signals(handlers.HandlerFinder(app_state))

window.show_all()

logging.debug('Entering main loop')
Gtk.main()
