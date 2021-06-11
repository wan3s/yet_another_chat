"""
Модуль, реализующий интерфейс работы с чатом.

:copyright: DreamTeam, 2021
"""

import argparse
import tkinter as tk

import common
import views


def main():
    """Return nothing. Connection to the chat.

    :return: nothing
    """
    ctx = common.create_context()
    root = tk.Tk()
    av = views.AuthView(root, ctx)
    root.mainloop()


if __name__ == '__main__':
    """Starting program."""
    main()
