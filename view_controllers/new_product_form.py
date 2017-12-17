import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class NewProduct(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Nuevo cliente")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.external_box)

        # Area nombre
        self.name_box = Gtk.Box()
        self.external_box.pack_start(self.name_box, False, False, 0)
        self.name_label = Gtk.Label("Nombre")
        self.name_box.pack_start(self.name_label, False, False, 0)
        self.name_entry = Gtk.Entry()
        self.name_box.pack_start(self.name_entry, False, False, 0)

        # Area tipo
        self.type_box = Gtk.Box()
        self.external_box.pack_start(self.type_box, False, False, 0)
        self.type_label = Gtk.Label("Tipo")
        self.type_box.pack_start(self.type_label, False, False, 0)
        self.type_entry = Gtk.Entry()
        self.type_box.pack_start(self.type_entry, False, False, 0)

        # Area descripcion
        self.description_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.external_box.pack_start(self.description_box, False, False, 0)
        self.description_label = Gtk.Label("Descripcion")
        self.description_box.pack_start(self.description_label, False, False, 0)
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_size_request(500, 100)
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        self.description_txt_view = Gtk.TextView()
        self.scrolled_window.add(self.description_txt_view)
        self.scrolled_window.set_margin_bottom(10)
        self.description_box.pack_start(self.scrolled_window, False, False, 0)

        # Area cantidad/precio
        self.forth_row_box = Gtk.Box()
        self.external_box.add(self.forth_row_box)
        self.amount_label = Gtk.Label("Cantidad")
        self.forth_row_box.pack_start(self.amount_label, False, False, 0)
        self.amount_entry = Gtk.Entry()
        self.forth_row_box.pack_start(self.amount_entry, False, False, 0)
        self.value_label = Gtk.Label("Precio")
        self.forth_row_box.pack_start(self.value_label, False, False, 0)
        self.value_entry = Gtk.Entry()
        self.forth_row_box.pack_start(self.value_entry, False, False, 0)
        self.symbol_label = Gtk.Label("€")
        self.forth_row_box.pack_start(self.symbol_label, False, False, 0)

        self.show_all()
        self.connect("delete_event", Gtk.main_quit)

if __name__ == "__main__":
    NewProduct()
    Gtk.main()
