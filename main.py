"""
The purpose of this program is to provide a method for a user to encode and
send a known number set over an unencrypted communications platform.
Users on both ends will need to know a predetermined index
number in order to decode the code-string into the correct number.
This program takes the user-defined number as input and uses a predetermined
code index in order to encode the number into a crypted string.  It also
provides the option to decode the code-string back into a number.
"""

from encoder_gui import EncodeGui
import tkinter as tk


def main():
    window = tk.Tk()
    EncodeGui(window)
    window.mainloop()


main()s
