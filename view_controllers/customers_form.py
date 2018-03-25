import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from models.customer import Customer
from models.purchase import Purchase



class CustomerForm(Gtk.Window):
    """ Customer form box using Gtk library.

    A box that will be displayed in the Notebook.
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="Clientes")
        self.set_default_size(600, 200)


        self.window_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        self.add(self.window_box)

        self.header = Gtk.HeaderBar(title = "Cliente")
        self.header.props.show_close_button = True
        self.set_titlebar(self.header)

        self.header_button_area = Gtk.Box()

        self.search_entry = Gtk.SearchEntry()
        self.search_entry.set_placeholder_text("Ej: 123456789")

        self.print_button = Gtk.Button()
        self.print_button.connect("clicked", self.on_ticket_clicked)
        self.icon = Gio.ThemedIcon(name="document-print")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.BUTTON)

        self.print_button.add(self.image)

        self.search_button = Gtk.Button()
        self.search_button.connect("clicked", self.on_search_clicked)
        self.icon = Gio.ThemedIcon(name="system-search")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.BUTTON)

        self.search_button.add(self.image)


        self.add_button = Gtk.Button()
        self.add_button.connect("clicked", self.on_new_client_clicked)
        self.icon = Gio.ThemedIcon(name="list-add")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.BUTTON)

        self.add_button.add(self.image)
        self.header_button_area.pack_end(self.print_button, False, False, 10)
        self.header_button_area.pack_end(self.add_button, False, False, 10)
        self.header_button_area.pack_end(self.search_button, False, False, 0)

        self.header.pack_end(self.header_button_area)
        self.header_button_area.pack_start(self.search_entry, False, False, 10)

        ################################################
        self.data_box = Gtk.Box()
        self.window_box.pack_start(self.data_box, False, False, 0)

        self.columns = ["DNI", "NOMBRE", "APELLIDOS", "DIRECCION", "CP", "TLF", "F.NACIMIENTO"]

        self.model = Gtk.ListStore(str, str, str, str, int, int, str)
        self.tree_view = Gtk.TreeView(model=self.model)
        self.data_box.pack_start(self.tree_view, False, False, 0)

        for item in range(len(self.columns)):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(self.columns[item], cell, text=item)
            self.tree_view.append_column(column)

        ################################################
        self.purchase_box = Gtk.Box()
        self.window_box.pack_start(self.purchase_box, False, False, 0)
        self.purchase_columns = ["DNI", "ID PRODUCTO", "FECHA"]

        self.purchase_model = Gtk.ListStore(str, int, str)
        self.purchase_tree_view = Gtk.TreeView(model=self.purchase_model)
        self.purchase_box.pack_start(self.purchase_tree_view, False, False, 0)

        for item in range(len(self.purchase_columns)):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(self.purchase_columns[item], cell, text=item)
            self.purchase_tree_view.append_column(column)



        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.connect("delete-event", self.destroy)
        self.show_all()


    def on_search_clicked(self, button):
        """ Search button event.

        Fills every field with the data on the database for the given
        user id.
        """

        self.model.clear()
        costumer = Customer(self.search_entry.get_text()) # New costumer object with the user id on search_entry
        costumer_list = costumer.get_customer() # Gets the database data
        if costumer_list == []:
            #self.validation_label.set_markup("<span color='red'>No existe ese usuario</span>")
            ''''''
        else:
            #self.validation_label.set_text("")
            for item in costumer_list:
                self.model.append(item)

        purchase = Purchase(self.search_entry.get_text()) # New purchase object with the user id on search_entry
        if purchase.check_purchase():
            #self.validation_label.set_text("")
            purchases = purchase.get_purchase_by_dni() # Gets the database data
            for item in purchases:
                self.purchase_model.append(item) # Appends the list to the Gtk.ListStore model
        else:
            #self.validation_label.set_markup("<span color='red'>No hay productos</span>")
            ''''''

    def on_new_client_clicked(self, button):
        """ Casts a new window."""
        from view_controllers.new_customer_form import NewCustomer
        NewCustomer()

    def on_ticket_clicked(self, button):
        from reportlab.platypus import Table
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors

        script = []
        table_header = [["Nombre", "Apellidos", "DNI"]]
        table = Table(table_header)
        table.setStyle([('INNERGRID', (0,0),(-1,-1), 0.25, colors.black),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black)])
        script.append(table)

        costumer = Customer(self.search_entry.get_text()) # New costumer object with the user id on search_entry
        costumer_list = costumer.get_customer() # Gets the database data
        if costumer_list == []:
            #self.validation_label.set_markup("<span color='red'>No existe ese usuario</span>")
            ''''''
        else:
            table = Table(costumer_list)
            table.setStyle([('BOX', (0,0),(-1,-1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])

        script.append(table)


        #creacion del archivo pdf
        doc = SimpleDocTemplate("cliente.pdf", pagesize=A4, showBoundary=1)
        doc.build(script)

