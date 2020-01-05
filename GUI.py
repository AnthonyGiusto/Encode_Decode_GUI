import tkinter as tk
from tkinter import *
from encode import Encode
from decode import Decode

#The purpose of this program is to provide a method for a user to encode and send a known number set
#over an unencrypted communications platform.  Users on both ends will need to know a predetermined index
#number in order to decode the code-string into the correct number.  
#
#This program takes the user-defined number as input and uses a predetermined code index in order to 
#encode the number into a crypted string.  It also provides the option to decode the code-string 
#back into a number.
#_______________________________________________________________________________________________


class EncodeGui:
	"""creates a GUI for the Encoder application"""

	def __init__(self, master):
		"""creates an instance of the EncodeGui class"""

		font=("corbel",9)

		self.master = master
		master.configure( bg = "darkblue")
		master.title("Encoder UI")
		master.geometry("335x135")

		#calls for a user entry for the index number
		self.index = Entry(window, width = 5)
		self.index.grid(column=7, row=4)

		self.index_number1 = Label(window, text="Enter Index",
			fg="white", bg="darkblue",font=font)
		self.index_number1.grid(column=5, row=4)
		#creates a label for the Number entry

		self.lbl_number1 = Label(window, text="Number",
			fg="white", bg="darkblue",font=font)
		self.lbl_number1.grid(column=1, row=2)
		
		#creates a label for the encode result
		self.lbl_code = Label(window, text="Encoded:",
			fg="white", bg="darkblue",font=font)
		self.lbl_code.grid(column =1, row = 4)

		#creates a placeholder for the encode result
		self.encode_blankentry = tk.Label(window, text="", bg = "darkblue")
		self.encode_blankentry.grid(column =2, row = 4)

		#creates a blankspace at position row =1, column = 1
		self.encode_blankspace = tk.Label(window, text="", bg = "darkblue")
		self.encode_blankspace.grid(column =1, row = 1)

		#calls for a user entry for the number to be encoded
		self.plain_txt = Entry(window, width = 15)
		self.plain_txt.grid(column=2, row=2)

		#creates a Encode button
		self.btn_encode = Button(text="Encode", 
			command=self.encode_click,fg = "white", bg = "black",font=font)
		self.btn_encode.grid(column=3, row=2)

		#creates a label for the Number entry
		self.lbl_code = Label(window, text="Code",
			fg="white", bg="darkblue",font= font)
		self.lbl_code.grid(column=1, row=6)

		#creates a label for the code result
		self.lbl_number2 = Label(window, text="Decoded:",
			fg="white", bg="darkblue",font= font)
		self.lbl_number2.grid(column =1, row = 7)

		#calls for a user entry for the code to be decoded
		self.code_entry = Entry(window, width = 15)
		self.code_entry.grid(column=2, row=6)

		#creates a Decode button
		self.btn_decode =Button(text="Decode", command=self.decode_click,
			fg = "white", bg = "black",font= font)
		self.btn_decode.grid(column=3, row=6)

		#creates a placeholder for the decode result
		self.decode_blankentry= tk.Label(window, text="", bg = "darkblue")
		self.decode_blankentry.grid(column =2, row = 7)
	
	def encode_click(self):
		"""Takes a user input value and encodes it with a predefined month index into a code-string"""
		index=int(self.index.get())
		number=str(self.plain_txt.get())
		encoded = Encode.encode(number,index)
		self.encode_blankentry.configure(text= encoded,fg="white")
	
	def decode_click(self):
		"""Takes a user input code-string and decodes it with a predefined month index into a number"""
		index=int(self.index.get())
		code=str(self.code_entry.get())
		decoded = Decode.decode(code,index)
		self.decode_blankentry.configure(text= decoded, fg="white")


window = Tk()
encode_gui = EncodeGui(window)
window.mainloop()