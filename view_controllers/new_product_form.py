import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.product import Product


class NewProduct(Gtk.Window):
    """ Product form window using Gtk library.

    A form that creates a new product in the database.
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="Nuevo producto")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.external_box)

        # id area
        self.id_box = Gtk.Box()
        self.external_box.pack_start(self.id_box, False, False, 0)
        self.id_label = Gtk.Label("ID")
        self.id_entry = Gtk.Entry()
        self.id_box.pack_end(self.id_entry, False, False, 0)
        self.id_box.pack_end(self.id_label, False, False, 10)

        # name area
        self.name_box = Gtk.Box()
        self.external_box.pack_start(self.name_box, False, False, 0)
        self.name_label = Gtk.Label("Nombre")
        self.name_label.set_margin_left(20)
        self.name_box.pack_start(self.name_label, False, False, 10)
        self.name_entry = Gtk.Entry()
        self.name_box.pack_start(self.name_entry, False, False, 0)

        # type area
        self.type_box = Gtk.Box()
        self.external_box.pack_start(self.type_box, False, False, 0)
        self.type_label = Gtk.Label("Tipo")
        self.type_label.set_margin_left(20)
        self.type_box.pack_start(self.type_label, False, False, 10)
        self.type_entry = Gtk.Entry()
        self.type_entry.set_margin_left(18)
        self.type_box.pack_start(self.type_entry, False, False, 0)

        # description area
        self.description_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.external_box.pack_start(self.description_box, False, False, 0)
        self.description_label = Gtk.Label("Descripcion")
        self.description_label.set_margin_top(10)
        self.description_label.set_margin_bottom(10)
        self.description_box.pack_start(self.description_label, False, False, 0)
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_size_request(500, 100)
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.ALWAYS)
        self.description_txt_view = Gtk.TextView()
        self.text_buffer = self.description_txt_view.get_buffer()
        self.scrolled_window.add(self.description_txt_view)
        self.scrolled_window.set_margin_bottom(10)
        self.description_box.pack_start(self.scrolled_window, False, False, 0)

        # quantity/price area
        self.forth_row_box = Gtk.Box()
        self.external_box.add(self.forth_row_box)
        self.amount_label = Gtk.Label("Cantidad")
        self.amount_label.set_margin_left(20)
        self.forth_row_box.pack_start(self.amount_label, False, False, 10)
        self.amount_entry = Gtk.Entry()
        self.forth_row_box.pack_start(self.amount_entry, False, False, 0)
        self.value_label = Gtk.Label("Precio")
        self.value_label.set_margin_left(20)
        self.forth_row_box.pack_start(self.value_label, False, False, 10)
        self.value_entry = Gtk.Entry()
        self.forth_row_box.pack_start(self.value_entry, False, False, 0)
        self.symbol_label = Gtk.Label("€")
        self.forth_row_box.pack_start(self.symbol_label, False, False, 5)

        # button area
        self.button_box = Gtk.Box()
        self.external_box.pack_start(self.button_box, False, False, 0)
        self.validate_button = Gtk.Button(label="Registrar")
        self.validate_button.set_margin_top(20)
        self.validate_button.connect("clicked", self.on_validate_button_clicked)
        self.button_box.pack_start(self.validate_button, False, False, 0)

        self.show_all()
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS) # Shows the current window centered on the screen.
        self.connect("delete_event", self.destroy)

    def on_validate_button_clicked(self, button):
        """ Validate button event

        Creates a new product in the products table.
        """
        id = self.id_entry.get_text()
        name = self.name_entry.get_text()
        type = self.type_entry.get_text()
        quantity = self.amount_entry.get_text()
        value = self.value_entry.get_text()
        description = self.text_buffer.get_text(self.text_buffer.get_start_iter(), self.text_buffer.get_end_iter(), True)
        product = Product(id, name, type, quantity, float(value), description)
        product.insert_product()
        self.destroy()

