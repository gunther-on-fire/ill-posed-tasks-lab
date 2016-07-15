import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('lab_16.glade')
handlers = {
	'OnDeleteWindow': Gtk.main_quit
}

builder.connect_signals(handlers)
window = builder.get_object('Main Window')
window.show_all()

Gtk.main()
