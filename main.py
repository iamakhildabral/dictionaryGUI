import tkinter as tk
from ttkbootstrap.scrolled import ScrolledText
import ttkbootstrap as ttk
from PyDictionary import PyDictionary

def explain_the_word():
    scrolled_text_output_box.insert(tk.END,"")
    user_entere_value = user_input.get()
    meaning_of_word = dictionary.meaning(user_entere_value)
    scrolled_text_output_box.insert(tk.END,meaning_of_word)

dictionary = PyDictionary()
window = ttk.Window(themename='darkly')
window.title("Dictionary Window")
window.geometry("600x500")
window.state("zoom")

# Label to Display above the entry box
user_info_label = ttk.Label(master=window,text="Enter your word here : ",font="Calibri 12")
user_info_label.pack(pady=20)

# Entry for the user to know the word meaning
user_input = ttk.Entry(master=window,font="Calibri 14")
user_input.pack(pady=10)

# A Button to explain the meaning of the word
explain_it = ttk.Button(master=window,text="Explain",command=explain_the_word)
explain_it.pack(pady=10)


# Scrolled Text box to explain the meaning of the word
scrolled_text_output_box = ScrolledText(master=window, padding=5, height=6, autohide=True)
scrolled_text_output_box.pack()






window.mainloop()