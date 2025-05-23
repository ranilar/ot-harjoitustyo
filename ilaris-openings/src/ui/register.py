from tkinter import ttk, StringVar, constants
from services.user_service import UsernameExistsError


class Register:
    def __init__(self, master, show_main_menu, handle_show_login, user_service):
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
        self._show_main_menu = show_main_menu
        self._handle_show_login = handle_show_login
        self._register_service = user_service
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
        """Handles register event.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()
        
        if len(username) == 0 or len(password) == 0:
            self._show_error("Username and password required.")
            return
        if len(username) >= 10 or len(username) <= 3:
            self._show_error("Username must be between 4 and 10 characters")
            return
        if 3 >= len(password):
            self._show_error("Password must be atleast 4 characters")
            return
        try:
            self._register_service.register(username, password, login=True)
            self._show_main_menu() 
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

        register_button = ttk.Button(master=self._frame, text="Create account", command=self._register_handler)
        login_button = ttk.Button(master=self._frame, text="I already have an account", command=self._handle_show_login)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        register_button.grid(padx=5, pady=5)
        login_button.grid(padx=5, pady=5)

        self._hide_error()