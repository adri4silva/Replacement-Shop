import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.costumer import Costumer


class NewCostumer(Gtk.Window):
    """ Customer form window using Gtk library.

    A form that creates a new costumer in the database.
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="Nuevo cliente")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.external_box)

        # name area
        self.name_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.name_box, False, False, 0)
        self.name_label = Gtk.Label("Nombre")
        self.name_label.set_margin_left(10)
        self.name_box.pack_start(self.name_label, False, False, 0)
        self.name_entry = Gtk.Entry()
        self.name_entry.set_margin_left(44)
        self.name_box.pack_start(self.name_entry, False, False, 0)

        # last name area
        self.last_name_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.last_name_box, False, False, 0)
        self.last_name_label = Gtk.Label("Apellido")
        self.last_name_label.set_margin_left(10)
        self.last_name_box.pack_start(self.last_name_label, False, False, 0)
        self.last_name_entry = Gtk.Entry()
        self.last_name_entry.set_margin_left(44)
        self.last_name_box.pack_start(self.last_name_entry, False, False, 0)

        # id area
        self.id_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.id_box, False, False, 0)
        self.id_label = Gtk.Label("DNI")
        self.id_label.set_margin_left(10)
        self.id_box.pack_start(self.id_label, False, False, 0)
        self.id_entry = Gtk.Entry()
        self.id_entry.set_margin_left(64)
        self.id_box.pack_start(self.id_entry, False, False, 0)
        self.id_letter_label = Gtk.Label("")
        self.id_box.pack_start(self.id_letter_label, False, False, 0)

        # address area
        self.address_box = Gtk.Box()
        self.external_box.pack_start(self.address_box, False, False, 0)
        self.address_label = Gtk.Label("Domicilio")
        self.address_label.set_margin_left(10)
        self.address_box.pack_start(self.address_label, False, False, 0)
        self.address_entry = Gtk.Entry()
        self.address_entry.set_margin_left(71)
        self.address_box.pack_start(self.address_entry, False, False, 0)

        # zip code area
        self.zip_box = Gtk.Box()
        self.external_box.pack_start(self.zip_box, False, False, 0)
        self.zip_label = Gtk.Label("C.P.")
        self.zip_label.set_margin_left(10)
        self.zip_box.pack_start(self.zip_label, False, False, 0)
        self.zip_entry = Gtk.Entry()
        self.zip_entry.set_margin_left(96)
        self.zip_box.pack_start(self.zip_entry, False, False, 0)

        # tlf area
        self.tlf_box = Gtk.Box()
        self.external_box.pack_start(self.tlf_box, False, False, 0)
        self.tlf_label = Gtk.Label("TLF")
        self.tlf_label.set_margin_left(10)
        self.tlf_box.pack_start(self.tlf_label, False, False, 0)
        self.tlf_entry = Gtk.Entry()
        self.tlf_entry.set_margin_left(100)
        self.tlf_box.pack_start(self.tlf_entry, False, False, 0)

        # birth date area
        self.birth_box = Gtk.Box()
        self.external_box.pack_start(self.birth_box, False, False, 0)
        self.birth_label = Gtk.Label("Fecha de Nacimiento")
        self.birth_label.set_margin_left(10)
        self.birth_box.pack_start(self.birth_label, False, False, 4)
        self.birth_entry = Gtk.Entry()
        self.birth_entry.set_visibility(False)
        self.birth_box.pack_start(self.birth_entry, False, False, 0)

        # button area
        self.button_box = Gtk.Box()
        self.external_box.pack_start(self.button_box, False, False, 0)
        self.validate_button = Gtk.Button(label="Registrar")
        self.validate_button.connect("clicked", self.on_validate_button_clicked)
        self.button_box.pack_start(self.validate_button, False, False, 0)

        self.show_all()
        self.connect("delete_event", Gtk.main_quit)

    def on_validate_button_clicked(self, button):
        """ Validate button event

        Creates a new costumer in the costumers table.
        """
        dni = self.id_entry.get_text()
        name = self.name_entry.get_text()
        last_name = self.last_name_entry.get_text()
        address = self.address_entry.get_text()
        postal_code = self.zip_entry.get_text()
        t_number = self.tlf_entry.get_text()
        costumer = Costumer(dni, name, last_name, address, postal_code, t_number)
        if costumer.insert_costumer(): # True
            self.destroy()
        else: # False
            '''Ya existe el usuario'''


