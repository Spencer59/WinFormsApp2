import customtkinter

customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")


label = customtkinter.CTkLabel(app, text="The main tab", fg_color="transparent")



def button_function():
    print("button pressed")


def button_function2():
    customtkinter.set_appearance_mode("dark") 

button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function2)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

def combobox_callback(choice):
    if choice == "option 1":
        customtkinter.set_appearance_mode("light")

combobox_var = customtkinter.StringVar(value="option 2")
combobox = customtkinter.CTkComboBox(app, values=["option 1", "option 2"],
                                     command=combobox_callback, variable=combobox_var)
combobox_var.set("option 2")


def combox_set():
    combobox.set(value="option 1")

    
combobox_var2 = combobox.cget(combobox_var)
    
if combobox_var2 == "option 1":
    combox_set(True)
    customtkinter.set_appearance_mode("light")
    




app.mainloop()
