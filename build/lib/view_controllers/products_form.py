import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
from models.product import Product


class ProductForm(Gtk.Window):
    """ Product form box using Gtk library.

    A box that will be displayed in the Notebook.
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="Products")
        self.set_default_size(650, 200)

        self.window_box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        self.add(self.window_box)

        self.header = Gtk.HeaderBar(title = "Producto")
        self.header.props.show_close_button = True
        self.set_titlebar(self.header)

        self.header_button_area = Gtk.Box()

        self.search_entry = Gtk.SearchEntry()
        self.search_entry.set_placeholder_text("Ej: 1")

        self.refresh_button = Gtk.Button()
        self.refresh_button.connect("clicked", self.on_refresh_clicked)
        self.icon = Gio.ThemedIcon(name="view-refresh")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.BUTTON)

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
        self.add_button.connect("clicked", self.on_new_product_clicked)
        self.icon = Gio.ThemedIcon(name="list-add")
        self.image = Gtk.Image.new_from_gicon(self.icon, Gtk.IconSize.BUTTON)

        self.add_button.add(self.image)
        self.header_button_area.pack_end(self.refresh_button, False, False, 10)
        self.header_button_area.pack_end(self.print_button, False, False, 10)
        self.header_button_area.pack_end(self.add_button, False, False, 10)
        self.header_button_area.pack_end(self.search_button, False, False, 0)

        self.header.pack_end(self.header_button_area)
        self.header_button_area.pack_start(self.search_entry, False, False, 10)

        ################################################
        self.data_box = Gtk.Box()
        self.window_box.pack_start(self.data_box, False, False, 0)

        self.columns = ["ID", "NOMBRE", "TIPO", "STOCK", "PRECIO", "DESCRIPCION"]
        self.model = Gtk.ListStore(int, str, str, int, int, str)
        self.tree_view = Gtk.TreeView(model = self.model)
        self.data_box.pack_start(self.tree_view, False, False, 0)

        for item in range(len(self.columns)):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(self.columns[item], cell, text=item)
            self.tree_view.append_column(column)
        product = Product(self.search_entry.get_text())
        products_list = product.get_products()
        for item in products_list:
            self.model.append(item)

        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.connect("delete-event", self.destroy)
        self.show_all()

    def on_new_product_clicked(self, button):
        """ New product button event.

        Creates a NewProduct window.
        """
        from view_controllers.new_product_form import NewProduct
        NewProduct()

    def on_search_clicked(self, button):
        """ Search button event.

        Retrieves data from the products table and adds that data
        into the Gtk.ListStore model of the Gtk.TreeView
        """
        self.model.clear()
        product_id = self.search_entry.get_text()
        products = Product(product_id)
        product_list = products.get_product_by_id()
        if product_list is not None:
            self.model.append(product_list)
            #self.validation_label.set_text("")
        else:
            #self.validation_label.set_markup("<span color='red'>No hay productos</span>")
            ''''''

    def on_ticket_clicked(self, button):
        from reportlab.platypus import Table
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors

        script = []
        table_header = [["ID", "NOMBRE", "TIPO", "STOCK", "PRECIO", "DESCRIPCION"]]
        table = Table(table_header)
        table.setStyle([('INNERGRID', (0,0),(-1,-1), 0.25, colors.black),
                ('BOX', (0,0), (-1,-1), 0.25, colors.black)])
        script.append(table)

        product = Product(self.search_entry.get_text()) # New costumer object with the user id on search_entry
        product_list = product.get_products() # Gets the database data
        if product_list == []:
            #self.validation_label.set_markup("<span color='red'>No existe ese usuario</span>")
            ''''''
        else:
            table = Table(product_list)
            table.setStyle([('BOX', (0,0),(-1,-1), 0.25, colors.black),
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])

            script.append(table)


        #creacion del archivo pdf
        doc = SimpleDocTemplate("productos.pdf", pagesize=A4, showBoundary=1)
        doc.build(script)

    def on_refresh_clicked(self, button):
        self.model.clear()
        product = Product(self.search_entry.get_text())
        products_list = product.get_products()
        for item in products_list:
            self.model.append(item)
