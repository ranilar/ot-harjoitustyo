from tkinter import ttk, StringVar, constants
from services.user_service import InvalidCredentialsError


class Login:
    def __init__(self, master, main_menu, handle_show_register, user_service):
        """
        UI View for logging in as a registered user.
        
        Args:
            master:
                The main TKinter element.
            main_menu:
                A function which is called after the login is succesful.
            handle_show_register:
                A function which is called when opening the register view.

        """
        self._root = master
        self._main_menu = main_menu
        self._handle_show_register = handle_show_register
        self._login_service = user_service
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

    def _login_handler(self):
        """Handles login event.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            self._login_service.login(username, password)
            self._main_menu()
        except InvalidCredentialsError:
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

        login_button = ttk.Button(master=self._frame, text="Login", command=self._login_handler)
        register_button = ttk.Button(master=self._frame, text="Create an account", command=self._handle_show_register)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5)
        register_button.grid(padx=5, pady=5)

        self._hide_error()