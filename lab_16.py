#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import logging

class Tab1Handler:

    def __init__(self, builder):
        self.logger = logging.getLogger('T1Handler')
        self.logger.debug('Created Tab1Handler')

        self.combobox_value = None
        self.x_number = 10

        self.button = builder.get_object('non-discret-graph')

        self._validate()

    def ChooseComboBoxValue(self, combobox):
        self.combobox_value =  combobox.get_model()[combobox.get_active()][0]
        self.logger.debug('New combobox value: %s' % self.combobox_value)

        self._validate()

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
        valid = self.combobox_value is not None and self.x_number is not None
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
window.show_all()

logging.debug('Entering main loop')
Gtk.main()
