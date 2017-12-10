import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class NewClient(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Nuevo cliente")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.external_box)

        # Area nombre
        self.name_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.name_box, False, False, 0)
        self.name_label = Gtk.Label("Nombre")
        self.name_box.pack_start(self.name_label, False, False, 0)
        self.name_entry = Gtk.Entry()
        self.name_box.pack_start(self.name_entry, False, False, 0)

        # Area apellidos
        self.last_name_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.last_name_box, False, False, 0)
        self.last_name_label = Gtk.Label("Apellido")
        self.last_name_box.pack_start(self.last_name_label, False, False, 0)
        self.last_name_entry = Gtk.Entry()
        self.last_name_box.pack_start(self.last_name_entry, False, False, 0)

        # Area dni
        self.id_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.id_box, False, False, 0)
        self.id_label = Gtk.Label("DNI")
        self.id_box.pack_start(self.id_label, False, False, 0)
        self.id_entry = Gtk.Entry()
        self.id_box.pack_start(self.id_entry, False, False, 0)
        self.id_letter_label = Gtk.Label("")
        self.id_box.pack_start(self.id_letter_label, False, False, 0)

        # Area domicilio
        self.address_box = Gtk.Box()
        self.external_box.pack_start(self.address_box, False, False, 0)
        self.address_label = Gtk.Label("Domicilio")
        self.address_box.pack_start(self.address_label, False, False, 0)
        self.address_entry = Gtk.Entry()
        self.address_box.pack_start(self.address_entry, False, False, 0)

        # Area codigo postal
        self.zip_box = Gtk.Box()
        self.external_box.pack_start(self.zip_box, False, False, 0)
        self.zip_label = Gtk.Label("C.P.")
        self.zip_box.pack_start(self.zip_label, False, False, 0)
        self.zip_entry = Gtk.Entry()
        self.zip_box.pack_start(self.zip_entry, False, False, 0)

        # Area telefono
        self.tlf_box = Gtk.Box()
        self.external_box.pack_start(self.tlf_box, False, False, 0)
        self.tlf_label = Gtk.Label("TLF")
        self.tlf_box.pack_start(self.tlf_label, False, False, 0)
        self.tlf_entry = Gtk.Entry()
        self.tlf_box.pack_start(self.tlf_entry, False, False, 0)

        # Area fecha nacimiento
        self.birth_box = Gtk.Box()
        self.external_box.pack_start(self.birth_box, False, False, 0)
        self.birth_label = Gtk.Label("Fecha de Nacimiento")
        self.birth_box.pack_start(self.birth_label, False, False, 0)
        self.birth_entry = Gtk.Entry()
        self.birth_entry.set_visibility(False)
        self.birth_box.pack_start(self.birth_entry, False, False, 0)

        # Area boton
        self.validate_button = Gtk.Button(label="Registrar")
        self.external_box.pack_start(self.validate_button, False, False, 0)

        self.show_all()
        self.connect("delete_event", Gtk.main_quit)

if __name__ == "__main__":
    NewClient()
    Gtk.main()
