import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.user import User




class LoginForm(Gtk.Window):
    """Logim form window using Gtk library.

    First window of the program.
    """
    def __init__(self):
        Gtk.Window.__init__(self, title="Login")

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.external_box)

        self.user_area()
        self.password_area()
        self.validation_label_area()
        self.button_area()

        self.show_all()
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS) # Shows the current window centered on the screen.
        self.connect("delete_event", Gtk.main_quit)


    def validate_user_clicked(self, button):
        """ Validate button event.

        Validates if the user is in the database. If it's inside, it creates a
        new Notebook Window. If it's not inside, displays a label.

        :param button: The button which the user has clicked.
        """
        username = self.user_entry.get_text()
        password = self.pwd_entry.get_text()
        validate_user = User(username, password, "a")

        if validate_user.check_user():
            self.destroy()
            from view_controllers.main_selection_menu import SelectionMenu
            SelectionMenu(username=username)
        else:
            self.validation_label.set_markup("<span color='red'>No existe el usuario</span>")


    def new_user_clicked(self, button):
        """New user button event.

        Creates a new RegisterForm Window.

        :param button: The button which the user has clicked.
        """
        from view_controllers.reg_form import RegisterForm
        self.hide() # Hide the current window
        RegisterForm(self)

    def user_area(self):
        # user area
        self.user_box = Gtk.Box(spacing=36)
        self.external_box.pack_start(self.user_box, False, False, 0)
        self.user_label = Gtk.Label()
        self.user_label.set_markup("<b>Usuario</b>")
        self.user_label.set_margin_left(30)
        self.user_box.pack_start(self.user_label, False, False, 0)
        self.user_entry = Gtk.Entry()
        self.user_box.pack_start(self.user_entry, False, False, 0)

    def password_area(self):
        # password area
        self.pwd_box = Gtk.Box(spacing=15)
        self.external_box.pack_start(self.pwd_box, False, False, 0)
        self.pwd_label = Gtk.Label()
        self.pwd_label.set_markup("<b>Contraseña</b>")
        self.pwd_label.set_margin_left(30)
        self.pwd_box.pack_start(self.pwd_label, False, False, 0)
        self.pwd_entry = Gtk.Entry()
        self.pwd_entry.set_visibility(False)
        self.pwd_box.pack_start(self.pwd_entry, False, False, 0)

    def validation_label_area(self):
        # validation label area
        self.label_box = Gtk.Box()
        self.external_box.pack_start(self.label_box, False, False, 0)
        self.validation_label = Gtk.Label("")
        self.validation_label.set_margin_left(90)
        self.label_box.pack_start(self.validation_label, False, False, 0)

    def button_area(self):
        # button area
        self.button_box = Gtk.Box()
        self.external_box.pack_start(self.button_box, False, False, 0)
        self.new_user_button = Gtk.Button(label = "Registro")
        self.new_user_button.connect("clicked", self.new_user_clicked)
        self.button_box.pack_start(self.new_user_button, False, False, 0)
        self.validate_button = Gtk.Button(label="Entrar")
        self.validate_button.connect("clicked", self.validate_user_clicked)
        self.button_box.pack_end(self.validate_button, False, False, 0)


if __name__ == "__main__":
    LoginForm()
    Gtk.main()
