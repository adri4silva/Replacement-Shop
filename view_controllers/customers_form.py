import gi
import datetime

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.costumer import Costumer
from models.purchase import Purchase


class CostumerForm(Gtk.Box):
    """ Costumer form box using Gtk library.

    A box that will be displayed in the Notebook.
    """
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=10)

        # search area
        self.search_box = Gtk.Box()
        self.pack_start(self.search_box, False, False, 0)
        self.search_label = Gtk.Label("BUSQUEDA DNI")
        self.search_entry = Gtk.Entry()
        self.search_box.pack_end(self.search_entry, False, False, 0)
        self.search_box.pack_end(self.search_label, False, False, 20)

        # data area
        self.data_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.data_box.set_margin_top(10)
        self.pack_start(self.data_box, False, False, 0)
        # first row
        self.first_row_box = Gtk.Box()
        self.data_box.pack_start(self.first_row_box, False, False, 0)
        self.name_label = Gtk.Label("Nombre")
        self.name_label.set_margin_left(10)
        self.first_row_box.pack_start(self.name_label, False, False, 10)
        self.name_entry = Gtk.Entry()
        self.name_entry.set_margin_left(6)
        self.first_row_box.pack_start(self.name_entry, False, False, 0)
        self.last_name_label = Gtk.Label("Apellido")
        self.last_name_label.set_margin_left(10)
        self.first_row_box.pack_start(self.last_name_label, False, False, 10)
        self.last_name_entry = Gtk.Entry()
        self.first_row_box.pack_start(self.last_name_entry, False, False, 0)
        # second row
        self.second_row_box = Gtk.Box()
        self.data_box.pack_start(self.second_row_box, False, False, 0)
        self.address_label = Gtk.Label("Domicilio")
        self.address_label.set_margin_left(10)
        self.second_row_box.pack_start(self.address_label, False, False, 10)
        self.address_entry = Gtk.Entry()
        self.second_row_box.pack_start(self.address_entry, False, False, 0)
        # third row
        self.third_row_box = Gtk.Box()
        self.data_box.pack_start(self.third_row_box, False, False, 0)
        self.zip_label = Gtk.Label("C.P.")
        self.zip_label.set_margin_left(10)
        self.third_row_box.pack_start(self.zip_label, False, False, 10)
        self.zip_entry = Gtk.Entry()
        self.zip_entry.set_margin_left(25)
        self.third_row_box.pack_start(self.zip_entry, False, False, 0)
        self.tlf_label = Gtk.Label("TLF")
        self.tlf_label.set_margin_left(10)
        self.third_row_box.pack_start(self.tlf_label, False, False, 10)
        self.tlf_entry = Gtk.Entry()
        self.tlf_entry.set_margin_left(20)
        self.third_row_box.pack_start(self.tlf_entry, False, False, 0)
        # forth row
        self.label = Gtk.Label("HISTORIAL COMPRA")
        self.label.set_margin_left(10)
        self.data_box.pack_start(self.label, False, False, 10)
        # fifth row
        self.columns = ["DNI", "ID PRODUCTO", "FECHA"]

        self.model = Gtk.ListStore(str, int, str)
        self.tree_view = Gtk.TreeView(model=self.model)
        self.data_box.pack_start(self.tree_view, False, False, 0)

        for item in range(len(self.columns)):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(self.columns[item], cell, text=item)
            self.tree_view.append_column(column)

        # button box
        self.button_box = Gtk.Box()
        self.button_box.set_margin_top(20)
        self.pack_start(self.button_box, False, False, 0)
        self.new_customer_button = Gtk.Button(label="NUEVO")
        self.new_customer_button.connect("clicked", self.on_new_client_clicked)
        self.button_box.pack_start(self.new_customer_button, False, False, 0)
        self.validate_button = Gtk.Button(label="BÚSQUEDA")
        self.validate_button.connect("clicked", self.on_search_clicked)
        self.button_box.pack_end(self.validate_button, False, False, 0)


    def on_search_clicked(self, button):
        """ Search button event.

        Fills every field with the data on the database for the given
        user id.
        """
        costumer = Costumer(self.search_entry.get_text()) # New costumer object with the user id on search_entry
        costumer_list = costumer.get_costumer() # Gets the database data
        self.name_entry.set_text(costumer_list[0][1])
        self.last_name_entry.set_text(costumer_list[0][2])
        self.address_entry.set_text(costumer_list[0][3])
        self.zip_entry.set_text(str(costumer_list[0][4]))
        self.tlf_entry.set_text(str(costumer_list[0][5]))
        purchase = Purchase(self.search_entry.get_text()) # New purchase object with the user id on search_entry
        purchases = purchase.get_purchase_by_dni() # Gets the database data
        p = (purchases[0], purchases[1], str(purchases[2])) # A list with (str, int, str)
        self.model.append(p) # Appends the list to the Gtk.ListStore model


    def on_new_client_clicked(self, button):
        """ Casts a new window."""
        from view_controllers.new_costumer_form import NewCostumer
        NewCostumer()

