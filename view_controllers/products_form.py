import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.product import Product


class ProductForm(Gtk.Box):
    """ Product form box using Gtk library.

    A box that will be displayed in the Notebook.
    """
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

        self.search_area()
        self.data_area()
        self.treeview_area()
        self.button_area()

    def on_new_product_selected(self, button):
        """ New product button event.

        Creates a NewProduct window.
        """
        from view_controllers.new_product_form import NewProduct
        NewProduct()

    def on_search_selected(self, button):
        """ Search button event.

        Retrieves data from the products table and adds that data
        into the Gtk.ListStore model of the Gtk.TreeView
        """
        self.model.clear()
        product_id = self.search_entry.get_text()
        products = Product(product_id)
        product_list = products.get_product_by_id()
        self.model.append(product_list)

    def search_area(self):
        # search area
        self.search_box = Gtk.Box()
        self.search_box.set_margin_bottom(20)
        self.pack_start(self.search_box, False, False, 0)
        self.search_label = Gtk.Label()
        self.search_label.set_markup("<b>BUSQUEDA ID</b>")
        self.search_entry = Gtk.Entry()
        self.search_box.pack_end(self.search_entry, False, False, 0)
        self.search_box.pack_end(self.search_label, False, False, 20)

    def data_area(self):
        # data area
        self.data_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.pack_start(self.data_box, False, False, 0)

    def treeview_area(self):
        # Treeview
        self.columns = ["ID", "NOMBRE", "TIPO", "STOCK", "PRECIO", "DESCRIPCION"]
        self.model = Gtk.ListStore(int, str, str, int, float, str)
        self.tree_view = Gtk.TreeView(model = self.model)
        self.data_box.pack_start(self.tree_view, False, False, 0)

        for item in range(len(self.columns)):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(self.columns[item], cell, text=item)
            self.tree_view.append_column(column)

    def button_area(self):
        # button area
        self.button_box = Gtk.Box()
        self.button_box.set_margin_top(204)
        self.pack_start(self.button_box, False, False, 0)
        self.new_product_button = Gtk.Button(label="NUEVO")
        self.new_product_button.connect("clicked", self.on_new_product_selected)
        self.button_box.pack_start(self.new_product_button, False, False, 0)
        self.search_button = Gtk.Button(label="BÚSQUEDA")
        self.search_button.connect("clicked", self.on_search_selected)
        self.button_box.pack_end(self.search_button, False, False, 0)
