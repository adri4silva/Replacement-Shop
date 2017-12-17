import gi
from view_controllers.customers_form import CostumerForm
from view_controllers.products_form import ProductForm
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Notebook(Gtk.Window):
    """ Notebook window using Gtk library.

    This window calls customers and products windows.
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="Recambios")

        self.notebook_layout = Gtk.Notebook()
        self.add(self.notebook_layout)
        self.products = ProductForm()
        self.customers = CostumerForm()

        self.notebook_layout.append_page(self.customers, Gtk.Label("Clientes"))
        self.notebook_layout.append_page(self.products, Gtk.Label("Productos"))

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

