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
mire_before_discretization_plot = builder.get_object('mire_before_discretization')

mire_before_discretization_figure = Figure(dpi=100)
mire_before_discretization = mire_before_discretization_figure.add_subplot(111)
mire_before_discretization_plot.add_with_viewport(FigureCanvas(mire_before_discretization_figure))

logging.debug('Configuring discrete plot')
mire_after_discretization_plot = builder.get_object('mire_after_discretization')

mire_after_discretization_figure = Figure(dpi=100)
mire_after_discretization = mire_after_discretization_figure.add_subplot(111)
mire_after_discretization_plot.add_with_viewport(FigureCanvas(mire_after_discretization_figure))

#Tab2

logging.debug('Calculating FFT of the input data')
fft_before_modification_plot = builder.get_object('fourier_image_before_modification')

fft_before_modification_figure = Figure(dpi=100)
fft_before_modification = fft_before_modification_figure.add_subplot(111)
fft_before_modification_plot.add_with_viewport(FigureCanvas(fft_before_modification_figure))

logging.debug('Configuring FFT of the input data')
fft_after_modification_plot = builder.get_object('fourier_image_after_modification')

fft_after_modification_figure = Figure(dpi=100)
fft_after_modification = fft_after_modification_figure.add_subplot(111)
fft_after_modification_plot.add_with_viewport(FigureCanvas(fft_after_modification_figure))

logging.debug('Connecting signals')
app_state.builder = builder
app_state.mire_before_discretization = mire_before_discretization
app_state.mire_after_discretization = mire_after_discretization
app_state.fft_before_modification = fft_before_modification
app_state.fft_after_modification = fft_after_modification

builder.connect_signals(handlers.HandlerFinder(app_state))

window.show_all()

logging.debug('Entering main loop')
Gtk.main()
