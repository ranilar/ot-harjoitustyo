from tkinter import ttk, StringVar, constants
from services.user_service import UserService, UsernameExistsError


class Register:
    def __init__(self, master, handle_register, handle_show_login):
        """
        UI View for registering as a new user.
        
        Args:
            master:
                The main TKinter element.
            handle_login:
                A function which is called after the register is succesful.
            handle_show_register:
                A function which is called when opening the main menu.

        """
        self._root = master
        self._handle_register = handle_register
        self._handle_show_create_user_view = handle_show_login
        self._register_service = UserService()
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self, *args, **kwargs):
        """Generates the view.
        """
        self._frame.pack(*args, **kwargs)


    def destroy(self):
        """Destroys the view.
        """
        self._frame.destroy()

    def _register_handler(self):
        """Handles login event.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password required.")

        try:
            self._register_service.register(username, password)
            self._handle_register()
        except UsernameExistsError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        """ Shows error message.

        Args:
            message: 
                The message string to display in the case of an error.
        """
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        """Hides error.
        """
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        """Creates username field.
        """
        username_label = ttk.Label(master=self._frame, text="Username")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5)
        self._username_entry.grid(padx=5, pady=5)

    def _initialize_password_field(self):
        """Creates password field.
        """
        password_label = ttk.Label(master=self._frame, text="Password")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5)
        self._password_entry.grid(padx=5, pady=5)

    def _initialize(self):
        """Creates the widgets for the login window.
        """
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(master=self._frame, textvariable=self._error_variable, foreground="red")

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        register_button = ttk.Button(master=self._frame, text="Register", command=self._register_handler)

        login_button = ttk.Button(master=self._frame, text="Login", command=self._handle_show_create_user_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        register_button.grid(padx=5, pady=5)
        login_button.grid(padx=5, pady=5)

        self._hide_error()