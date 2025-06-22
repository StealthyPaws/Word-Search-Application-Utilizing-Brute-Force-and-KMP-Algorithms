from tkinter import *
import tkinter as tk

# creating Main Window
root = tk.Tk()
root.title("String Matching GUI")
root.geometry("2000x2000")
bg_image = PhotoImage(file="PIC1.png")
# root.configure(bg="lightblue")
background_label = Label(root, image=bg_image)
background_label.place(x=0, y=0,relheight=1) 
# background_label.pack()

# below 4 lines will make sure the display is centered
# root.grid_rowconfigure(0, weight=1)  
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(0, weight=1)  
# root.grid_columnconfigure(1, weight=1) 
# root.grid_columnconfigure(2, weight=1)
findwhat = '\0'
# first label of find what
findwhat_label = Label(root,text="Find What: ",font=("Times New Roman", 30,"bold"),bg='lightpink')
findwhat_label.grid(row=22, column=1, padx=25, pady=50)
# findwhat_label.pack(pady=40,padx=40)
# findwhat_label.grid(row=5, column=3, padx=10, pady=10
# now create a input entry text
findwhat_entry = Entry(root, font=("Times New Roman", 20),bg='lightpink')  
findwhat_entry.grid(row=22, column=2, padx=1,pady=45) 
# findwhat_entry.pack()
def get_text():
    findwhat = findwhat_entry.get()
    print(findwhat)
    
def clear_input():
    # when clear button will be clicked we will empty the text written on 
    # text box
    findwhat_entry.delete(0, END)
# findwhat_entry.grid(row=5, column=5, padx=10, pady=10)
# now I will create a button to the left of findwhat_entry
findwhat_button = Button(root, text="Find Next", font=("Times New Roman", 20),bg='lightpink',highlightbackground="lightpink",highlightcolor="lightpink",highlightthickness=5,borderwidth=0,command=get_text)           
# findwhat_button.grid(row=0, column=1, padx=10, pady=10)
# findwhat_button.grid(row=0, column=2, padx=13, pady=13,sticky="w")
findwhat_button.grid(row=22, column=3, padx=2, pady=40)
# findwhat_button.pack()
# next button of cancel
# by pressing cancel we will automatically erase the content written in the text box
cancel_button = tk.Button(root, text="Cancel", font=("Times New Roman", 20),bg='lightpink',highlightbackground="lightpink",highlightcolor="lightpink",highlightthickness=5,borderwidth=0,command=clear_input)         
cancel_button.grid(row=22, column=4)
# cancel_button.pack()
# checkbox for Match Whole Word Only
match_whole_word = IntVar()
checkbox = Checkbutton(root, text="Match Whole Word Only", variable=match_whole_word, font=("Times New Roman", 20), bg='lightpink')
checkbox.grid(row=23, column=2,pady=0)
# checkbox.grid(row=1, column=1, pady=13,sticky="n")
# checkbox.pack()
# for matching String Cases
match_case = IntVar()
checkbox2 = Checkbutton(root, text="Match Case", variable=match_case, font=("Times New Roman", 20), bg='lightpink')
checkbox2.grid(row=24,column=2,padx=20,pady=20)
root.mainloop()
