import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from models.user import User

class RegisterForm(Gtk.Window):
    """ Registration form window using Gtk library.

    This window is used to create a new user in the database.
    """
    def __init__(self, login):
        Gtk.Window.__init__(self, title="Registro")
        self.login = login

        self.user_type = "a" # User type. Value "a" by default.

        self.external_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.external_box)

        self.user_area()
        self.password_area()
        self.validation_label_area()
        self.radio_buttons_area()
        self.button_area()

        self.show_all()
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS) # Shows the current window centered on the screen.
        self.connect("delete_event", Gtk.main_quit)

    def on_validate_user_clicked(self, button):
        """ Validate button event.

        Validates if the user is in the database. If it's inside, it shows
        the login form window and destroys the current window. If it's not
        inside, displays a label.

        :param button: The button which the user has clicked.
        """
        username = self.user_entry.get_text()
        pwd = self.pwd_entry.get_text()
        new_user = User(username, pwd, self.user_type)
        if new_user.insert_user() == True:
            self.destroy()
            self.login.set_visible(True)
        else: # False
            self.validation_label.set_markup("<span color='red'>Ya existe ese usuario</span>")

    def on_user_type_toggled(self, button, message):
        """ Radio Buttons event.

        Checks which button has activated the event and changes the
        user type variable according to the message event.

        :param button: The button which the user has clicked.
        :param message: The message event of the button.
        """
        if button.get_active(): # True
            self.user_type = message


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
        self.label_box.set_margin_top(10)
        self.external_box.pack_start(self.label_box, False, False, 0)
        self.validation_label = Gtk.Label("")
        self.validation_label.set_margin_left(110)
        self.label_box.pack_start(self.validation_label, False, False, 0)

    def radio_buttons_area(self):
        # radio buttons area
        self.radio_buttons_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.radio_buttons_box.set_margin_top(20)
        self.external_box.pack_start(self.radio_buttons_box, False, False, 0)
        self.account_label = Gtk.Label("TIPO DE CUENTA", xalign=0)
        self.radio_buttons_box.pack_start(self.account_label, False, False, 0)
        self.user_admin = Gtk.RadioButton.new_with_label(None, "Admin")
        self.user_employee = Gtk.RadioButton.new_from_widget(self.user_admin)
        self.user_employee.set_label("Dependiente")
        self.user_employee.connect("toggled", self.on_user_type_toggled, "e")
        self.user_admin.connect("toggled", self.on_user_type_toggled, "a")
        self.radio_buttons_box.pack_start(self.user_admin, False, False, 0)
        self.radio_buttons_box.pack_start(self.user_employee, False, False, 0)

    def button_area(self):
        # buttons area
        self.button_box = Gtk.Box()
        self.external_box.pack_start(self.button_box, False, False, 0)
        self.validate_button = Gtk.Button(label="Registrar")
        self.validate_button.connect("clicked", self.on_validate_user_clicked)
        self.button_box.pack_end(self.validate_button, False, False, 0)






