import gi
from views.customers_form import CustomerForm
from views.products_form import ProductForm
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Notebook(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Recambios")

        self.notebook_layout = Gtk.Notebook()  # Creacion do notebook
        self.add(self.notebook_layout)  # Engadimos o notebook a ventana

        self.notebook_layout.append_page(CustomerForm(), Gtk.Label("Clientes"))
        self.notebook_layout.append_page(ProductForm(), Gtk.Label("Productos"))

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Notebook()
    Gtk.main()
