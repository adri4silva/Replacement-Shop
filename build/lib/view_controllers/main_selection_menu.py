import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class SelectionMenu(Gtk.Window):
    def __init__(self, username):
        Gtk.Window.__init__(self, title="Selection Menu")

        self.username = username

        self.set_border_width(5)
        self.set_resizable = False

        self.grid_layout = Gtk.Grid()
        self.add(self.grid_layout)

        self.header = Gtk.HeaderBar(title="Recambios")
        self.header.props.show_close_button = True
        self.set_titlebar(self.header)

        self.user_image = Gtk.Image()
        self.user_image.set_from_file("../images/user.png")

        self.product_image = Gtk.Image()
        self.product_image.set_from_file("../images/barcode.png")


        self.welcome_message = Gtk.Label("Bienvenido, {name}".format(name=self.username))
        self.welcome_message.set_margin_bottom(50)
        self.welcome_message.set_margin_top(30)
        self.grid_layout.attach(self.welcome_message, 2, 1, 1, 2)


        self.user_menu_button = Gtk.Button()
        self.user_menu_button.add(self.user_image)
        self.user_menu_button.connect("clicked", self.on_customer_form_clicked)
        self.grid_layout.attach(self.user_menu_button, 1, 3, 1, 2)

        self.product_menu_button = Gtk.Button()
        self.product_menu_button.add(self.product_image)
        self.product_menu_button.connect("clicked", self.on_product_form_clicked)
        self.grid_layout.attach(self.product_menu_button, 3, 3, 1, 2)

        self.user_label = Gtk.Label("Usuarios")
        self.user_label.set_margin_top(15)
        self.grid_layout.attach(self.user_label, 1, 5, 1, 1)
        self.product_label = Gtk.Label("Productos")
        self.product_label.set_margin_top(15)
        self.grid_layout.attach(self.product_label, 3, 5, 1, 1)






        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_customer_form_clicked(self, button):
        from view_controllers.customers_form import CustomerForm
        CustomerForm()

    def on_product_form_clicked(self, button):
        from view_controllers.products_form import ProductForm
        ProductForm()
