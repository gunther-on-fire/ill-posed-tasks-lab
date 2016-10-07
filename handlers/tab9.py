import logging
import numpy as np
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk


class Handler:
    def __init__(self, app):
        self.logger = logging.getLogger('Tab9Handler')
        self.logger.debug('Created Tab9Handler')

        self.app = app

        # Populating default values by explicitly calling on-change callbacks
        self.onChangedAlpha(app.builder.get_object('alpha_spinbutton'))

        # Get objects
        self.app.tab_9_store = self.app.builder.get_object('liststoreStep9')
        self.app.tab_9_treestore = self.app.builder.get_object('treeviewStep9')

        # Sorting liststore by the 1st column
        self.app.tab_9_store.set_sort_column_id(0, Gtk.SortType.ASCENDING)

        self.app.alpha_array = np.array([])
        self.app.error_array = np.array([])


    def onChangedAlpha(self, alpha):
        self.app.alpha = round(float(alpha.get_value()), 6)
        self.logger.debug('New alpha value is %s' % self.app.alpha)

    def onDeleteARow(self, button):
        selection = self.app.tab_9_treestore.get_selection()

        model, paths = selection.get_selected_rows()

        self.logger.debug('Row # ' + str([p.to_string() for p in paths]) + ' has been deleted')

        for p in reversed(paths):
            itr = model.get_iter(p)
            model.remove(itr)

    def onDeleteAllRows(self, button):
        self.app.tab_9_store.clear()

    def updateErrorAlphaPlot(self, button):

        # Clearing the plot area
        self.app.regularization.cla()

        self.app.alpha_array = np.array([])
        self.app.error_array = np.array([])

        for row in self.app.tab_9_store:
           self.app.alpha_array = np.append(self.app.alpha_array, row[0])

        for row in self.app.tab_9_store:
           self.app.error_array = np.append(self.app.error_array, row[1])

        self.app.regularization.grid(True)
        self.app.regularization.plot(self.app.alpha_array, self.app.error_array)

    def updateReconstructionPlot(self, button):

        # Clearing the plot area
        self.app.reconstructed_signal.cla()

        self.app.reconstructed_signal.grid(True)
        self.app.reconstructed_signal.set_xlim(0, self.app.m_value)
        self.app.reconstructed_signal.set_ylim(0, self.app.L_value + 50)

        self.app.reconstructed_signal.plot(self.app.discrete_input_x, self.app.inverse_fft_input_y)

        self.app.omega = 2 * np.pi * self.app.fft_input_x / self.app.x_value

        self.app.reconstructed_input_fft = np.fft.rfft(self.app.output_y + self.app.noise_y) / \
        (self.app.norm_ampl_fft_fwhl_y + self.app.alpha * (1 + self.app.omega ** 2) / self.app.norm_ampl_fft_fwhl_y)

        self.app.reconstructed_input_y = np.fft.irfft(self.app.reconstructed_input_fft)

        self.app.reconstructed_signal.plot(self.app.discrete_input_x, self.app.reconstructed_input_y)

        # Calculating the absolute error
        # sqrt (sum((sig_in - sig_reconstructed) ** 2) / number_of_counts) -- the standard deviation
        self.app.absolute_error = (sum((self.app.discrete_input_y - self.app.reconstructed_input_y) ** 2) /
                                   len(self.app.discrete_input_x)) ** 0.5

        # Calculating the mean value of the input signal, max/2
        self.app.mean_discrete_input_y = max(self.app.discrete_input_y) / 2

        # Calculating the relative error
        self.app.relative_error = (self.app.absolute_error / self.app.mean_discrete_input_y) * 100

        # Adding a row with all necessary data
        self.app.tab_9_store.append([self.app.alpha, self.app.absolute_error, self.app.relative_error])
