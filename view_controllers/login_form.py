import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.user import User


class LoginForm(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Login")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.external_box)

        # Area usuario
        self.user_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.user_box, False, False, 0)
        self.user_label=Gtk.Label("Usuario")
        self.user_label.set_margin_left(30)
        self.user_box.pack_start(self.user_label, False, False, 0)
        self.user_entry=Gtk.Entry()
        self.user_box.pack_start(self.user_entry, False, False, 0)

        # Area contraseña
        self.pwd_box = Gtk.Box(spacing=15)
        self.external_box.pack_start(self.pwd_box, False, False, 0)
        self.pwd_label=Gtk.Label("Contraseña")
        self.pwd_label.set_margin_left(30)
        self.pwd_box.pack_start(self.pwd_label, False, False, 0)
        self.pwd_entry=Gtk.Entry()
        self.pwd_entry.set_visibility(False)
        self.pwd_box.pack_start(self.pwd_entry, False, False, 0)

        # Area label comprobacion
        self.label_box = Gtk.Box()
        self.external_box.pack_start(self.label_box, False, False, 0)
        self.validation_label = Gtk.Label("")
        self.validation_label.set_margin_left(90)
        self.label_box.pack_start(self.validation_label, False, False, 0)

        # Area Botones
        self.button_box = Gtk.Box()
        self.external_box.pack_start(self.button_box, False, False, 0)
        self.new_user_button = Gtk.Button(label="Nuevo")
        self.new_user_button.connect("clicked", self.on_new_user_clicked)
        self.button_box.pack_start(self.new_user_button, False, False, 0)
        self.validate_button = Gtk.Button(label="Entrar")
        self.validate_button.connect("clicked", self.on_validate_user_clicked)
        self.button_box.pack_end(self.validate_button, False, False, 0)


        self.show_all()
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.connect("delete_event", Gtk.main_quit)

    def on_validate_user_clicked(self, button):
        username = self.user_entry.get_text()
        password = self.pwd_entry.get_text()
        validate_user = User(username, password, "a")
        if validate_user.check_user():
            self.validation_label.set_markup("<span color='red'>Usuario Correcto</span>")
            self.destroy()
            from views.notebook import Notebook
            Notebook()
        else:
            self.validation_label.set_markup("<span color='red'>No existe el usuario</span>")


    def on_new_user_clicked(self, button):
        from views.reg_form import RegisterForm
        self.hide()
        RegisterForm(self)


if __name__ == "__main__":
    LoginForm()
    Gtk.main()