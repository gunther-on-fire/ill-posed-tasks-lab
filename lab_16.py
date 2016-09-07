#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

import handlers

# Creating an empty class to store variables and 
# to make Tab(n)Handler classes communicate with each other
class Application():
    pass


logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s] %(message)s', level=logging.DEBUG)
logging.info('Starting application')

logging.debug('Loading UI from glade file')
builder = Gtk.Builder()
builder.add_from_file('lab_pt1.glade')

logging.debug('Showing main window')
window = builder.get_object('Main Window')

# Tab1

# Non-discrete part

logging.debug('Configuring non-discrete plot')
# Getting GtkScrolledWindow from the glade file
non_discrete_input_sw = builder.get_object('mire_before_discretization')
# Creating an instance of a matplotlib.figure and defining its resolution (dpi) 
non_discrete_input_fig = Figure(dpi=100)
# Adding a subplot to the plot
# 111 means that we have a 1 x 1 grid and are putting the subplot in the 1st cell
non_discrete_input_subplot = non_discrete_input_fig.add_subplot(111)
# Creating an instance of a FigureCanvasGTK3Cairo with our figure included in it
non_discrete_input_canvas = FigureCanvas(non_discrete_input_fig) 
# and then embedding it into the GtkScrolledWindow
non_discrete_input_sw.add_with_viewport(non_discrete_input_canvas)

# Discrete part

logging.debug('Configuring discrete plot')

discrete_input_sw = builder.get_object('mire_after_discretization')
discrete_input_fig = Figure(dpi=100)
discrete_input_subplot = discrete_input_fig.add_subplot(111)
discrete_input_canvas = FigureCanvas(discrete_input_fig) 
discrete_input_sw.add_with_viewport(discrete_input_canvas)

# Tab2

logging.debug('Configuring FFT plot')
fft_initial_sw = builder.get_object('fourier_image_before_modification')
fft_initial_fig = Figure(dpi=100)
fft_initial_canvas = FigureCanvas(fft_initial_fig) 
fft_initial_subplot = fft_initial_fig.add_subplot(111)
fft_initial_sw.add_with_viewport(fft_initial_canvas)

logging.debug('Configuring plot after modification')
fft_modified_sw = builder.get_object('fourier_image_after_modification')
fft_modified_fig = Figure(dpi=100)
fft_modified_canvas = FigureCanvas(fft_modified_fig) 
fft_modified_subplot = fft_modified_fig.add_subplot(111)
fft_modified_sw.add_with_viewport(fft_modified_canvas)

# Tab 3

logging.debug('Configuring FWHL non-discrete plot')
non_discrete_fwhl_sw = builder.get_object('fwhl_non_discrete')
non_discrete_fwhl_fig = Figure(dpi=100)
non_discrete_fwhl_canvas = FigureCanvas(non_discrete_fwhl_fig) 
non_discrete_fwhl_subplot = non_discrete_fwhl_fig.add_subplot(111)
non_discrete_fwhl_sw.add_with_viewport(non_discrete_fwhl_canvas)

logging.debug('Configuring FWHL discrete plot')
discrete_fwhl_sw = builder.get_object('fwhl_discrete')
discrete_fwhl_fig = Figure(dpi=100)
discrete_fwhl_canvas = FigureCanvas(discrete_fwhl_fig) 
discrete_fwhl_subplot = discrete_fwhl_fig.add_subplot(111)
discrete_fwhl_sw.add_with_viewport(discrete_fwhl_canvas)

# Tab 4

logging.debug('Configuring fourier image of FWHL discrete plot')
fft_fwhl_sw = builder.get_object('fwhl_fourier')
fft_fwhl_fig = Figure(dpi=100)
fft_fwhl_canvas = FigureCanvas(fft_fwhl_fig) 
fft_fwhl_subplot = fft_fwhl_fig.add_subplot(111)
fft_fwhl_sw.add_with_viewport(fft_fwhl_canvas)

# Tab5

logging.debug('Configuring fourier image of FWHL discrete plot')
output_signal_sw = builder.get_object('output_mire')
output_signal_fig = Figure(dpi=100)
output_signal_canvas = FigureCanvas(output_signal_fig) 
output_signal_subplot = output_signal_fig.add_subplot(111)
output_signal_sw.add_with_viewport(output_signal_canvas)

# Tab6

logging.debug('Configuring output mire with noise plot')
output_signal_with_noise_sw = builder.get_object('output_mire_with_noise')
output_signal_with_noise_fig = Figure(dpi=100)
output_signal_with_noise_canvas = FigureCanvas(output_signal_with_noise_fig) 
output_signal_with_noise_subplot = output_signal_with_noise_fig.add_subplot(111)
output_signal_with_noise_sw.add_with_viewport(output_signal_with_noise_canvas)

# Tab 7

logging.debug('Configuring FFT spectra of the output signal and noise plot')
output_and_noise_fft_sw = builder.get_object('output_and_noise_spectra')
output_and_noise_fft_fig = Figure(dpi=100)
output_and_noise_fft_canvas = FigureCanvas(output_and_noise_fft_fig) 
output_and_noise_fft_subplot = output_and_noise_fft_fig.add_subplot(111)
output_and_noise_fft_sw.add_with_viewport(output_and_noise_fft_canvas)


# Creating an instance of the uniting class

app = Application()

# A list of Tab(n)Handlers attributes

app.builder = builder

# Tab1Handler

app.non_discrete_input = non_discrete_input_subplot
app.discrete_input = discrete_input_subplot

# Tab2Handler

app.fft_initial = fft_initial_subplot
app.fft_modified = fft_modified_subplot

# Tab3Handler

app.non_discrete_fwhl = non_discrete_fwhl_subplot
app.discrete_fwhl = discrete_fwhl_subplot

# Tab4Handler

app.fft_fwhl = fft_fwhl_subplot

# Tab5Handler

app.output_signal = output_signal_subplot

# Tab6Handler

app.output_signal_with_noise = output_signal_with_noise_subplot

# Tab7Handler

app.output_and_noise_fft = output_and_noise_fft_subplot

logging.debug('Connecting signals')
builder.connect_signals(handlers.HandlerFinder(app))

window.show_all()

logging.debug('Entering main loop')
Gtk.main()
