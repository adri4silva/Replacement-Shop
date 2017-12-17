import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class ProductForm(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

        # Area busqueda
        self.search_box = Gtk.Box()
        self.pack_start(self.search_box, False, False, 0)
        self.search_label = Gtk.Label("BUSQUEDA ID")
        self.search_box.pack_start(self.search_label, False, False, 0)
        self.search_entry = Gtk.Entry()
        self.search_box.pack_start(self.search_entry, False, False, 0)

        # Area datos
        self.data_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.pack_start(self.data_box, False, False, 0)
        # Treeview
        self.columns = ["ID", "NOMBRE", "PRECIO", "TIPO", "STOCK", "DESCRIPCION"]
        self.tree_view = Gtk.TreeView() # Falta el modelo
        self.data_box.pack_start(self.tree_view, False, False, 0)

        for item in range(len(self.columns)):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(self.columns[item], cell, text=item)
            self.tree_view.append_column(column)

        # Boton
        self.button_box = Gtk.Box()
        self.pack_start(self.button_box, False, False, 0)
        self.new_product_button = Gtk.Button(label="NUEVO")
        self.button_box.pack_start(self.new_product_button, False, False, 0)
        self.basket_button = Gtk.Button(label="+ CARRITO")
        self.button_box.pack_end(self.basket_button, False, False, 0)
