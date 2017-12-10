import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CustomerForm(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

        # Area busqueda
        self.search_box = Gtk.Box()
        self.pack_start(self.search_box, False, False, 0)
        self.search_label = Gtk.Label("BUSQUEDA DNI")
        self.search_box.pack_start(self.search_label, False, False, 0)
        self.search_entry = Gtk.Entry()
        self.search_box.pack_start(self.search_entry, False, False, 0)

        # Area datos
        self.data_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.pack_start(self.data_box, False, False, 0)
        # Primera fila
        self.first_row_box = Gtk.Box()
        self.data_box.pack_start(self.first_row_box, False, False, 0)
        self.name_label = Gtk.Label("Nombre")
        self.first_row_box.pack_start(self.name_label, False, False, 0)
        self.name_entry = Gtk.Entry()
        self.first_row_box.pack_start(self.name_entry, False, False, 0)
        self.last_name_label = Gtk.Label("Apellido")
        self.first_row_box.pack_start(self.last_name_label, False, False, 0)
        self.last_name_entry = Gtk.Entry()
        self.first_row_box.pack_start(self.last_name_entry, False, False, 0)
        # Segunda fila
        self.second_row_box = Gtk.Box()
        self.data_box.pack_start(self.second_row_box, False, False, 0)
        self.address_label = Gtk.Label("Domicilio")
        self.second_row_box.pack_start(self.address_label, False, False, 0)
        self.address_entry = Gtk.Entry()
        self.second_row_box.pack_start(self.address_entry, False, False, 0)
        # Tercera fila
        self.third_row_box = Gtk.Box()
        self.data_box.pack_start(self.third_row_box, False, False, 0)
        self.zip_label = Gtk.Label("C.P.")
        self.third_row_box.pack_start(self.zip_label, False, False, 0)
        self.zip_entry = Gtk.Entry()
        self.third_row_box.pack_start(self.zip_entry, False, False, 0)
        self.tlf_label = Gtk.Label("TLF")
        self.third_row_box.pack_start(self.tlf_label, False, False, 0)
        self.tlf_entry = Gtk.Entry()
        self.third_row_box.pack_start(self.tlf_entry, False, False, 0)
        # Cuarta fila
        self.label = Gtk.Label("HISTORIAL COMPRA")
        self.data_box.pack_start(self.label, False, False, 0)
        # Quinta fila
        self.columns = ["ID", "NOMBRE", "PRECIO", "TIPO", "STOCK", "DESCRIPCION"]
        self.tree_view = Gtk.TreeView() # Falta el modelo
        self.data_box.pack_start(self.tree_view, False, False, 0)

        for item in range(len(self.columns)):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(self.columns[item], cell, text=item)
            self.tree_view.append_column(column)

        # Boton
        self.new_customer_button = Gtk.Button(label="NUEVO")
        self.pack_start(self.new_customer_button, False, False, 0)



