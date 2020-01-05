import tkinter as tk
from tkinter import *
from encode import Encode
from decode import Decode

class EncodeGui:

	def __init__(self, master):
		self.master = master
		master.title("Encode_GUI")
		master.geometry("375x105")

		#calls for a user entry for the index number
		self.index = Entry(window, width = 5)
		self.index.grid(column=7, row=3)

		self.index_number1 = Label(window, text="Index")
		self.index_number1.grid(column=5, row=3)
		#creates a label for the Number entry

		self.lbl_number1 = Label(window, text="Number")
		self.lbl_number1.grid(column=1, row=1)
		
		#creates a label for the encode result
		self.lbl_code = Label(window, text="Encoded")
		self.lbl_code.grid(column =1, row = 3)

		#creates a placeholder for the encode result
		self.encode_blankentry = tk.Label(window, text="")
		self.encode_blankentry.grid(column =2, row = 3)

		#calls for a user entry for the number to be encoded
		self.plain_txt = Entry(window, width = 15)
		self.plain_txt.grid(column=2, row=1)

		#creates a Encode button
		self.btn_encode = Button(text="Encode", command=self.encode_click,fg = "white", bg = "black")
		self.btn_encode.grid(column=3, row=1)

		#creates a label for the Number entry
		self.lbl_code = Label(window, text="Code")
		self.lbl_code.grid(column=1, row=5)

		#creates a label for the code result
		self.lbl_number2 = Label(window, text="Decoded")
		self.lbl_number2.grid(column =1, row = 6)


		#calls for a user entry for the code to be decoded
		self.code_entry = Entry(window, width = 15)
		self.code_entry.grid(column=2, row=5)

		#creates a Decode button
		self.btn_decode = Button(text="Decode", command=self.decode_click,fg = "white", bg = "black")
		self.btn_decode.grid(column=3, row=5)

		#creates a placeholder for the decode result
		self.decode_blankentry= tk.Label(window, text="")
		self.decode_blankentry.grid(column =2, row = 6)
	

	def encode_click(self):
		"""Takes a user input value and encodes it with a predefined month index into a code-string"""
		index=int(self.index.get())
		number=str(self.plain_txt.get())
		encoded = Encode.encode(number,index)
		self.encode_blankentry.configure(text= encoded)
	
	def decode_click(self):
		"""Takes a user input code-string and decodes it with a predefined month index into a number"""
		index=int(self.index.get())
		code=str(self.code_entry.get())
		decoded = Decode.decode(code,index)
		self.decode_blankentry.configure(text= decoded)


window = Tk()
encode_gui = EncodeGui(window)
window.mainloop()