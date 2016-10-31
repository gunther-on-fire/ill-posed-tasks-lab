#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar

import handlers

# Creating an empty class to store variables and 
# to make Tab(n)Handler classes communicate with each other
class Application():
    pass


logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s] %(message)s', level=logging.DEBUG)
logging.info('Starting the application')

logging.debug('Loading UI from glade file')
builder = Gtk.Builder()
builder.add_from_file('lab16_1.glade')

logging.debug('Showing the main window')
window = builder.get_object('main_window')

# Tab1

# Loading formulas

formula1_1 = builder.get_object('formula1_1')
formula1_1.set_from_file('./images/formula1_1.png')

formula1_2 = builder.get_object('formula1_2')
formula1_2.set_from_file('./images/formula1_2.png')

# Non-discrete part

logging.debug('Configuring the non-discrete plot')
# Getting GtkScrolledWindow from the glade file
non_discrete_input_sw = builder.get_object('tab1_scrolledwindow1')
# Creating an instance of a matplotlib.figure and defining its resolution (dpi) 
non_discrete_input_fig = Figure(figsize=(5,2))
# Adding a subplot to the plot
# 111 means that we have a 1 x 1 grid and are putting the subplot in the 1st cell
non_discrete_input_subplot = non_discrete_input_fig.add_subplot(111)
# Creating an instance of a FigureCanvasGTK3Cairo with our figure included in it
non_discrete_input_canvas = FigureCanvas(non_discrete_input_fig) 
# and then embedding it into the GtkScrolledWindow
non_discrete_input_sw.add_with_viewport(non_discrete_input_canvas)

# Embedding a toolbar from matplotlib library
toolbar1_1 = NavigationToolbar(non_discrete_input_canvas, window)
non_discrete_input_toolbar = builder.get_object('tab1_scrolledwindow2_toolbar1')
non_discrete_input_toolbar.add_with_viewport(toolbar1_1)

# Discrete part

logging.debug('Configuring the discrete plot')

discrete_input_sw = builder.get_object('tab1_scrolledwindow3')
discrete_input_fig = Figure(figsize=(5,2))
discrete_input_subplot = discrete_input_fig.add_subplot(111)
discrete_input_canvas = FigureCanvas(discrete_input_fig) 
discrete_input_sw.add_with_viewport(discrete_input_canvas)

toolbar1_2 = NavigationToolbar(discrete_input_canvas, window)
discrete_input_toolbar = builder.get_object('tab1_scrolledwindow4_toolbar2')
discrete_input_toolbar.add_with_viewport(toolbar1_2)

# Tab2

# Loading formulas

formula2_1 = builder.get_object('formula2_1')
formula2_1.set_from_file('./images/formula2_1.png')

formula2_2 = builder.get_object('formula2_2')
formula2_2.set_from_file('./images/formula2_2.png')

formula2_3 = builder.get_object('formula2_3')
formula2_3.set_from_file('./images/formula2_3.png')

logging.debug('Configuring the FFT plot')
fft_initial_sw = builder.get_object('tab2_scrolledwindow1')
fft_initial_fig = Figure(figsize=(5,2))
fft_initial_canvas = FigureCanvas(fft_initial_fig) 
fft_initial_subplot = fft_initial_fig.add_subplot(111)
fft_initial_sw.add_with_viewport(fft_initial_canvas)

toolbar2_1 = NavigationToolbar(fft_initial_canvas, window)
fft_initial_toolbar = builder.get_object('tab2_scrolledwindow2_toolbar1')
fft_initial_toolbar.add_with_viewport(toolbar2_1)

logging.debug('Configuring the plot after modification')
fft_modified_sw = builder.get_object('tab2_scrolledwindow3')
fft_modified_fig = Figure(figsize=(5,2))
fft_modified_canvas = FigureCanvas(fft_modified_fig) 
fft_modified_subplot = fft_modified_fig.add_subplot(111)
fft_modified_sw.add_with_viewport(fft_modified_canvas)

toolbar2_2 = NavigationToolbar(fft_modified_canvas, window)
fft_modified_toolbar = builder.get_object('tab2_scrolledwindow4_toolbar2')
fft_modified_toolbar.add_with_viewport(toolbar2_2)

# Tab3

# Loading formulas

formula3_1 = builder.get_object('formula3_1')
formula3_1.set_from_file('./images/formula3_1.png')

formula3_2 = builder.get_object('formula3_2')
formula3_2.set_from_file('./images/formula3_2.png')

formula3_3 = builder.get_object('formula3_3')
formula3_3.set_from_file('./images/formula3_3.png')

formula3_4 = builder.get_object('formula3_4')
formula3_4.set_from_file('./images/formula3_4.png')

formula3_5 = builder.get_object('formula3_5')
formula3_5.set_from_file('./images/formula2_2.png') # the same formula with Tab2

# FWHL parameters

logging.debug('Configuring the FWHL non-discrete plot')
non_discrete_fwhl_sw = builder.get_object('tab3_scrolledwindow1')
non_discrete_fwhl_fig = Figure(figsize=(5,2))
non_discrete_fwhl_canvas = FigureCanvas(non_discrete_fwhl_fig) 
non_discrete_fwhl_subplot = non_discrete_fwhl_fig.add_subplot(111)
non_discrete_fwhl_sw.add_with_viewport(non_discrete_fwhl_canvas)

toolbar3_1 = NavigationToolbar(non_discrete_fwhl_canvas, window)
non_discrete_fwhl_toolbar = builder.get_object('tab3_scrolledwindow3_toolbar1')
non_discrete_fwhl_toolbar.add_with_viewport(toolbar3_1)

logging.debug('Configuring the FWHL discrete plot')
discrete_fwhl_sw = builder.get_object('tab3_scrolledwindow2')
discrete_fwhl_fig = Figure(figsize=(5,2))
discrete_fwhl_canvas = FigureCanvas(discrete_fwhl_fig) 
discrete_fwhl_subplot = discrete_fwhl_fig.add_subplot(111)
discrete_fwhl_sw.add_with_viewport(discrete_fwhl_canvas)

toolbar3_2 = NavigationToolbar(discrete_fwhl_canvas, window)
discrete_fwhl_toolbar = builder.get_object('tab3_scrolledwindow4_toolbar2')
discrete_fwhl_toolbar.add_with_viewport(toolbar3_2)

# FFT of the FWHL

logging.debug('Configuring the fourier image of the FWHL discrete plot')
fft_fwhl_sw = builder.get_object('tab3_scrolledwindow5')
fft_fwhl_fig = Figure(figsize=(5,2))
fft_fwhl_canvas = FigureCanvas(fft_fwhl_fig) 
fft_fwhl_subplot = fft_fwhl_fig.add_subplot(111)
fft_fwhl_sw.add_with_viewport(fft_fwhl_canvas)

toolbar3_3 = NavigationToolbar(fft_fwhl_canvas, window)
fft_fwhl_toolbar = builder.get_object('tab3_scrolledwindow6_toolbar3')
fft_fwhl_toolbar.add_with_viewport(toolbar3_3)

# Tab4

# Loading formulas

formula4_1 = builder.get_object('formula4_1')
formula4_1.set_from_file('./images/formula4_1.png')

formula4_2 = builder.get_object('formula4_2')
formula4_2.set_from_file('./images/formula4_2.png')

formula4_3 = builder.get_object('formula4_3')
formula4_3.set_from_file('./images/formula4_3.png')

formula4_4 = builder.get_object('formula4_4')
formula4_4.set_from_file('./images/formula4_4_1.png')

formula4_5 = builder.get_object('formula4_5')
formula4_5.set_from_file('./images/formula4_5_1.png')

formula4_6 = builder.get_object('formula4_6')
formula4_6.set_from_file('./images/formula4_6_1.png')

formula4_7 = builder.get_object('formula4_7')
formula4_7.set_from_file('./images/formula4_7_1.png')

formula4_8 = builder.get_object('formula4_8')
formula4_8.set_from_file('./images/formula4_8_1.png')

# The output signal without any noise

logging.debug('Configuring the output signal plot')
output_signal_sw = builder.get_object('tab4_scrolledwindow1')
output_signal_fig = Figure(figsize=(5,2))
output_signal_canvas = FigureCanvas(output_signal_fig) 
output_signal_subplot = output_signal_fig.add_subplot(111)
output_signal_sw.add_with_viewport(output_signal_canvas)

toolbar4_1 = NavigationToolbar(output_signal_canvas, window)
output_signal_toolbar = builder.get_object('tab4_scrolledwindow2_toolbar1')
output_signal_toolbar.add_with_viewport(toolbar4_1)

# The output signal with the noise

logging.debug('Configuring the output mire with the noise plot')
output_signal_with_noise_sw = builder.get_object('tab4_scrolledwindow3')
output_signal_with_noise_fig = Figure(figsize=(5,2))
output_signal_with_noise_canvas = FigureCanvas(output_signal_with_noise_fig) 
output_signal_with_noise_subplot = output_signal_with_noise_fig.add_subplot(111)
output_signal_with_noise_sw.add_with_viewport(output_signal_with_noise_canvas)

toolbar4_2 = NavigationToolbar(output_signal_with_noise_canvas, window)
output_signal_with_noise_toolbar = builder.get_object('tab4_scrolledwindow4_toolbar2')
output_signal_with_noise_toolbar.add_with_viewport(toolbar4_2)


# Tab5

# Loading formulas

formula5_1 = builder.get_object('formula5_1')
formula5_1.set_from_file('./images/formula5_1.png')

formula5_2 = builder.get_object('formula5_2')
formula5_2.set_from_file('./images/formula5_2.png')

logging.debug('Configuring FFT spectra of the output signal and noise plot')
output_and_noise_fft_sw = builder.get_object('tab5_scrolledwindow1_spectra_signal_noise')
output_and_noise_fft_fig = Figure(figsize=(5,2))
output_and_noise_fft_canvas = FigureCanvas(output_and_noise_fft_fig)
output_and_noise_fft_subplot = output_and_noise_fft_fig.add_subplot(111)
output_and_noise_fft_sw.add_with_viewport(output_and_noise_fft_canvas)

toolbar5 = NavigationToolbar(output_and_noise_fft_canvas, window)
output_and_noise_fft_toolbar = builder.get_object('tab5_scrolledwindow2_toolbar1')
output_and_noise_fft_toolbar.add_with_viewport(toolbar5)

# Tab6

# Loading formulas

formula6_1 = builder.get_object('formula6_1')
formula6_1.set_from_file('./images/formula6_1.png')

formula6_2 = builder.get_object('formula6_2')
formula6_2.set_from_file('./images/formula6_2.png')

formula6_3 = builder.get_object('formula6_3')
formula6_3.set_from_file('./images/formula6_3.png')

formula6_4 = builder.get_object('formula6_4')
formula6_4.set_from_file('./images/formula6_4.png')

formula6_5 = builder.get_object('formula6_5')
formula6_5.set_from_file('./images/formula6_5.png')

# Tab7

# Loading formulas

formula7_1 = builder.get_object('formula7_1')
formula7_1.set_from_file('./images/formula7_1.png')

formula7_2 = builder.get_object('formula7_2')
formula7_2.set_from_file('./images/formula7_2.png')

formula7_3 = builder.get_object('formula7_3')
formula7_3.set_from_file('./images/formula7_3.png')

formula7_4 = builder.get_object('formula7_4')
formula7_4.set_from_file('./images/formula7_4.png')

formula7_5 = builder.get_object('formula7_5')
formula7_5.set_from_file('./images/formula7_5.png')

# The reconstructed signal part

logging.debug('Configuring the reconstructed signal plot')
reconstructed_signal_sw = builder.get_object('tab7_scrolledwindow1')
reconstructed_signal_fig = Figure(figsize=(5,2))
reconstructed_signal_canvas = FigureCanvas(reconstructed_signal_fig) 
reconstructed_signal_subplot = reconstructed_signal_fig.add_subplot(111)
reconstructed_signal_sw.add_with_viewport(reconstructed_signal_canvas)

toolbar7_1 = NavigationToolbar(reconstructed_signal_canvas, window)
reconstructed_signal_toolbar = builder.get_object('tab7_scrolledwindow2')
reconstructed_signal_toolbar.add_with_viewport(toolbar7_1)

# Regularization coefficient part

logging.debug('Configuring error vs alpha plot')
regularization_sw = builder.get_object('tab7_scrolledwindow3')
regularization_fig = Figure(figsize=(5,2))
regularization_canvas = FigureCanvas(regularization_fig) 
regularization_subplot = regularization_fig.add_subplot(111)
regularization_sw.add_with_viewport(regularization_canvas)

toolbar7_2 = NavigationToolbar(regularization_canvas, window)
regularization_toolbar = builder.get_object('tab7_scrolledwindow4')
regularization_toolbar.add_with_viewport(toolbar7_2)

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

app.fft_initial.set_xlabel(r'$i$', fontsize = 12, labelpad = -5)
app.fft_initial.set_ylabel(r'$Ф_{in}(i)$', fontsize = 12)
app.fft_initial.grid(True)

app.fft_modified.set_xlabel(r'$i$', fontsize = 12, labelpad = -5)
app.fft_modified.set_ylabel(r'$Ф_{in}(i)$', fontsize = 12)
app.fft_modified.grid(True)

# Tab3Handler

app.non_discrete_fwhl = non_discrete_fwhl_subplot
app.discrete_fwhl = discrete_fwhl_subplot
app.fft_fwhl = fft_fwhl_subplot

app.non_discrete_fwhl.set_xlabel(r'$x_i$', fontsize = 12, labelpad = -5)
app.non_discrete_fwhl.set_ylabel(r'$g(x_i)$', fontsize = 12, labelpad = -5)
app.non_discrete_fwhl.grid(True)

app.discrete_fwhl.set_xlabel(r'$i$', fontsize = 12, labelpad = -5)
app.discrete_fwhl.set_ylabel(r'$g(x_i)$', fontsize = 12, labelpad = -5)
app.discrete_fwhl.grid(True)

app.fft_fwhl.set_xlabel(r'$i$', fontsize = 12, labelpad = -5)
app.fft_fwhl.set_ylabel(r'$K(ω_i)$', fontsize = 12, labelpad = -5)
app.fft_fwhl.grid(True)

# Tab4Handler

app.output_signal = output_signal_subplot
app.output_signal.set_xlabel(r'$i$', fontsize = 12, labelpad = -2)
app.output_signal.set_ylabel(r'$E_{con}(x_i)$', fontsize = 12)
app.output_signal.grid(True)

app.output_signal_with_noise = output_signal_with_noise_subplot
app.output_signal_with_noise.set_xlabel(r'$i$', fontsize = 12, labelpad = -2)
app.output_signal_with_noise.set_ylabel(r'$E_{out}(x_i)$', fontsize = 12)
app.output_signal_with_noise.grid(True)

# Tab5Handler

app.output_and_noise_fft = output_and_noise_fft_subplot

app.output_and_noise_fft.set_ylabel('Ф(ω)', fontsize = 12)
app.output_and_noise_fft_RIGHT = app.output_and_noise_fft.twinx()
app.output_and_noise_fft_RIGHT.set_yticklabels([])
app.output_and_noise_fft_RIGHT.set_ylabel('N(ω)', fontsize = 12)
app.output_and_noise_fft.grid(True)

# Tab7Handler

app.reconstructed_signal = reconstructed_signal_subplot
app.regularization = regularization_subplot

app.reconstructed_signal.set_xlabel(r'$x_i$', fontsize = 12, labelpad = -5)
app.reconstructed_signal.set_ylabel(r'$E(x_i)$', fontsize = 12)
app.reconstructed_signal.grid(True)

app.regularization.set_xlabel('α', fontsize = 12, labelpad = -5)
app.regularization.set_ylabel('Ошибка, отн. ед.', fontsize = 12)
app.regularization.grid(True)

# Setting the initial parameters  
# for the alpha adjustment
# Can't be handled by Glade
alpha_adjustment = app.builder.get_object('tab7_adjustment_alpha')
alpha_adjustment.set_lower(0.00001)
alpha_adjustment.set_value(0.01)
alpha_adjustment.set_upper(10)
alpha_adjustment.set_step_increment(0.05)

logging.debug('Connecting signals')
builder.connect_signals(handlers.HandlerFinder(app))

window.show_all()

logging.debug('Entering main loop')
Gtk.main()
