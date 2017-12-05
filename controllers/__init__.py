def on_validate_user_clicked(self, button):
        username = self.user_entry.get_text()
        password = self.pwd_entry.get_text()
        if (username, password):# == select.check_user(username=username, password=password):
            self.validation_label.set_markup("<span color='red'>Usuario Correcto</span>")
        else:
            self.validation_label.set_markup("<span color='red'>No existe el usuario</span>")

def on_new_user_clicked(self):
    ''''''
