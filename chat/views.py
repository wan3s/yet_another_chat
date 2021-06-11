import tkinter as tk

class BaseView:
    def __init__(self, root):
        self._root = root

class AuthView(BaseView):
    def __init__(self, root, ctx):
        super().__init__(root)
        self._root.title('Authorization')
        self._root.geometry('400x100')
        self._ctx = ctx

        self._configure_rows()
        self._bind_conrtols()

    def _configure_rows(self):
        self._root.rowconfigure(0, weight=1)
        self._root.rowconfigure(1, weight=1)
        self._root.rowconfigure(3, weight=1)
        self._root.columnconfigure(0, weight=1)
        self._root.columnconfigure(1, weight=1)

    def _bind_conrtols(self):
        self._login_label = tk.Label(self._root, text='Login')
        self._password_label = tk.Label(self._root, text='Password')
        self._login_label.grid(row=0, column=0, sticky='w')
        self._password_label.grid(row=0, column=1, sticky='w')

        login = tk.StringVar()
        password = tk.StringVar()

        self._login_entry = tk.Entry(self._root, textvariable=login)
        self._password_entry = tk.Entry(self._root, textvariable=password)
        self._login_entry.grid(row=1, column=0, sticky='w')
        self._password_entry.grid(row=1, column=1, sticky='w')


        self._enter_button = tk.Button(
            self._root,
            text='Enter',
            command=(lambda: self._ctx.login_user(login.get(), password.get()))
        )
        self._reg_button = tk.Button(
            self._root,
            text='Register',
            command=(lambda: self._ctx.create_new_user(login.get(), password.get()))
        )
        self._enter_button.grid(row=2, column=0, sticky='w')
        self._reg_button.grid(row=2, column=1, sticky='w')
