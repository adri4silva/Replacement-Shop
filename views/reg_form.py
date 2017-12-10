import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Register_Form(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Registro")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.external_box)

        # Area nombre
        self.name_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.name_box, False, False, 0)
        self.name_label=Gtk.Label("Nombre")
        self.name_box.pack_start(self.name_label, False, False, 0)
        self.name_entry=Gtk.Entry()
        self.name_box.pack_start(self.name_entry, False, False, 0)

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

        # Area radiobuttons
        self.radio_buttons_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.external_box.pack_start(self.radio_buttons_box, False, False, 0)
        self.account_label = Gtk.Label("TIPO DE CUENTA", xalign=0)
        self.radio_buttons_box.pack_start(self.account_label, False, False, 0)

        self.user_admin = Gtk.RadioButton.new_with_label(None, "Admin")
        self.user_employee = Gtk.RadioButton.new_from_widget(self.user_admin)
        self.user_employee.set_label("Dependiente")
        #self.user_employee.connect("toggled", self.on_button_toggled, "descuento")
        #self.user_admin.connect("toggled", self.on_button_toggled, "descuento")

        self.radio_buttons_box.pack_start(self.user_employee, False, False, 0)
        self.radio_buttons_box.pack_start(self.user_admin, False, False, 0)

        # Area Boton
        self.button_box = Gtk.Box()
        self.external_box.pack_start(self.button_box, False, False, 0)
        self.validate_button = Gtk.Button(label="Entrar")
        #self.validate_button.connect("clicked", controller.on_validate_user_clicked)
        self.button_box.pack_end(self.validate_button, False, False, 0)



        self.show_all()
        self.connect("delete_event", Gtk.main_quit)



if __name__ == "__main__":
    Register_Form()
    Gtk.main()
