import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def ComboBoxChoice(combobox):
    #import ipdb; ipdb.set_trace()
    txt = combobox.get_model()[combobox.get_active()]
    print(txt[0])

def ChangedEntry(button):
    entry = builder.get_object('X length_entry')
    number = int(entry.get_text())
    print(number)

builder = Gtk.Builder()
builder.add_from_file('lab_step1.glade')
handlers = {
    'OnDeleteWindow': Gtk.main_quit,
    'OnChange': ComboBoxChoice,
    'OnEntryChange': ChangedEntry
}

builder.connect_signals(handlers)
window = builder.get_object('Main Window')
window.show_all()

Gtk.main()
