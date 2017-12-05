import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.select import Select

class Initial_Form(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Recambios")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.external_box)

        # Area usuario
        self.user_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.user_box, False, False, 0)
        self.user_label=Gtk.Label("Usuario")
        self.user_box.pack_start(self.user_label, False, False, 0)
        self.user_entry=Gtk.Entry()
        self.user_box.pack_start(self.user_entry, False, False, 0)

        # Area contraseña
        self.pwd_box = Gtk.Box(spacing=15)
        self.external_box.pack_start(self.pwd_box, False, False, 0)
        self.pwd_label=Gtk.Label("Contraseña")
        self.pwd_box.pack_start(self.pwd_label, False, False, 0)
        self.pwd_entry=Gtk.Entry()
        self.pwd_entry.set_visibility(False)
        self.pwd_box.pack_start(self.pwd_entry, False, False, 0)

        # Area label comprobacion
        self.label_box = Gtk.Box()
        self.external_box.pack_start(self.label_box, False, False, 0)
        self.validation_label = Gtk.Label("")
        self.label_box.pack_start(self.validation_label, False, False, 0)

        # Area Botones
        self.button_box = Gtk.Box()
        self.external_box.pack_start(self.button_box, False, False, 0)
        self.new_user_button = Gtk.Button(label="Nuevo")
        #self.new_user_button.connect("clicked", self.on_new_user_clicked)
        self.button_box.pack_start(self.new_user_button, False, False, 0)
        self.validate_button = Gtk.Button(label="Entrar")
        self.validate_button.connect("clicked", self.on_validate_user_clicked)
        self.button_box.pack_end(self.validate_button, False, False, 0)


        self.show_all()
        self.connect("delete_event", Gtk.main_quit)

    def on_validate_user_clicked(self, button):
        username = self.user_entry.get_text()
        password = self.pwd_entry.get_text()
        if (username, password) == Select().check_user(username=username, password=password):
            self.validation_label.set_markup("<span color='red'>Usuario Correcto</span>")
        else:
            self.validation_label.set_markup("<span color='red'>No existe el usuario</span>")

if __name__ == "__main__":
    Initial_Form()
    Gtk.main()
