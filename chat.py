from tkinter import *
import customtkinter
import openai
import os
import pickle


root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry('600x560')
root.iconbitmap('ai_lt.ico') 

#Submit to ChatGPT
def speak():
	if chat_entry.get():
		#Define our filename
		filename = "api_key"

		try:
			if os.path.isfile(filename):
				#Open the file
				input_file = open(filename, 'rb')

				#Load the data from file into a variable
				stuff = pickle.load(input_file)

				# Query ChatGPT
				#Define API key to ChatGPT
				openai.api_key = stuff

				#Create an install
				openai.Model.list()

				#Define our query / response
				response = openai.Completion.create(
					model = "text-davinci-002",
					prompt = chat_entry.get(),
					temperature = 0,
					max_tokens = 60,
					top_p = 1.0,
					frequency_penalty=0.0,
					presence_penalty=0.0
				)

				my_text.insert(END, response["choices"] [0] ["text"], strip())
				my_text.insert(END, "\n\n")

			else:
				#Create the file
				input_file = open(filename, 'wb')

				#Close the file
				input_file.close()
				#Error message
				my_text.insert(END, "\n\n You need an API key to talk with ChatGPT. Get one here: \n https://beta.openai.com/account/api-keys")

		except Exception as e:
			my_text.insert(END, f"\n\n There was an error \n\n{e}")

	else: 
		my_text.insert(END, "\n\n Hey! You Forgot to Type Anything!")

#Clear Screen
def clear():
	#Clear the main text box
	my_text.delete(1.0, END)

	#Clear the query entry widget
	chat_entry.delete(0, END)

#Do API Stuff
def key():
	#Define our filename
	filename = "api_key"

	try:
		if os.path.isfile(filename):
			#Open the file
			input_file = open(filename, 'rb')

			#Load the data from file into a variable
			stuff = pickle.load(input_file)

			# Output stuff to our entry box
			api_entry.insert(END, stuff)
		else:
			#Create the file
			input_file = open(filename, 'wb')

			#Close the file
			input_file.close()

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error \n\n{e}")

	#Reshow API Frame and Resize App
	root.geometry('600x710')
	api_frame.pack(pady=30)


#Save The API Key
def save_key():
	#Define our filename
	filename = "api_key"

	try:
		#Open file
		output_file = open(filename, 'wb')

		#Add the data to the file
		pickle.dump(api_entry.get(), output_file)

		#Delete Entrybox
		api_entry.delete(0, END)

		#Hide API Frame and Resize App
		api_frame.pack_forget()
		root.geometry('600x560')

	except Exception as e:
		my_text.insert(END, f"\n\n There was an error \n\n{e}")

#Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

#Add Text Widget To Get ChatGPT Response
my_text = Text(text_frame, 
	bg="#1c1c1d",
	width=65,
	bd=1,
	fg="#dcdcdd",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")
my_text.grid(row=0, column=0)

#Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
	command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

#Add Scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)


#Add Entry widget
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Type anything to ChatGPT",
	width=535,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)

#Create Button Frame
button_frame = customtkinter.CTkFrame(root,)
button_frame.pack(pady=10)


#Create Button

#Submit Button
submit_button = customtkinter.CTkButton(button_frame,
	text="Speak to ChatGPT",
	command=speak)
submit_button.grid(row=0, column=0, padx=25)

#Clear Button
clear_button = customtkinter.CTkButton(button_frame,
	text="Clear Response",
	command=clear)
clear_button.grid(row=0, column=1, padx=35)

#API Button
api_button = customtkinter.CTkButton(button_frame,
	text="Update API Key",
	command=key)
api_button.grid(row=0, column=2, padx=25)

#Add API Key
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=10)

#Add API entry widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enter your API key",
	width=350, height=50, border_width=1)
api_entry.grid(row=0, column=0, padx=20, pady=20)

#Add API Button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save Key",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)





root.mainloop()

