import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def ComboBoxChoice(combobox):
	print('Онотоле — краб!')
	txt = combobox.get_active()
	print(txt)


builder = Gtk.Builder()
builder.add_from_file('lab_step1.glade')
handlers = {
	'OnDeleteWindow': Gtk.main_quit,
	'OnChange': ComboBoxChoice
}

builder.connect_signals(handlers)
window = builder.get_object('Main Window')
window.show_all()

Gtk.main()
