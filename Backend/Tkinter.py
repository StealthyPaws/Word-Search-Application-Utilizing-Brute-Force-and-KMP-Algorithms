# importing the required libraries
from tkinter import *
import tkinter as tk
import string
import numpy as np
import time
import re
canvas_bg_color = "white"
def prefix_function(p):
    m = len(p)
    prefix = np.zeros(m, dtype='int')
    prefix[0] = 0
    k = 0
    # print(p[k+1])
    for q in range(1,m):
        while k > 0 and p[k] != p[q]:
            k = prefix[k-1]
        if p[k] == p[q]:
            k += 1
        prefix[q] = k
        # print(k, prefix)
    return prefix.astype('int')


def create_scrollable_frame(root):
    # Create a frame for the canvas and scrollbar
    main_frame = tk.Frame(root)
    main_frame.grid(row=25, column=2, columnspan=8)
    # Create a canvas
    canvas = tk.Canvas(main_frame, width=600, height=400, bg="white",bd=2, highlightthickness=2, highlightbackground="white", borderwidth=2)
    # canvas = tk.Canvas(main_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    # Create a vertical scrollbar linked to the canvas
    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # Configure the canvas to use the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    # Create a frame inside the canvas
    output_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=output_frame, anchor="nw")
    # Update scroll region when the frame is resized
    def configure_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    output_frame.bind("<Configure>", configure_scrollregion)
    return output_frame

def kmp_gui(text):
        # create window
        root = tk.Tk()
        root.title("String Matching GUI")
        root.geometry("2000x2000")
        root.bg_image = PhotoImage(file="C:\\Users\\User\\Downloads\\PIC1.png")
        image = root.bg_image
        background_label = Label(root, image=root.bg_image)
        background_label.place(x=0, y=0,relheight=1) 
        output_frame = create_scrollable_frame(root)
        canvas_bg_color = "white"
        def kmp_matcher(s, p,case_sensitive=False, as_whole=True):
            start_time = time.time()
            row_count = 1
            if not case_sensitive:
                s = s.lower()
                p = p.lower()
            n = len(s)
            m = len(p)
            prefix = prefix_function(p)
            q = 0
            found, found_whole = 0,0
            rownum, colnum, docnum = 1,0,0
            for i in range(n):
                if s[i] == '\n':
                    rownum +=1
                    colnum = 0
                if s[i] == "^":
                    docnum += 1
                    rownum, colnum = 1,0
                while q > 0  and p[q] != s[i]:
                    q = prefix[q-1]
                if p[q] == s[i]:
                    q +=1
                if q == m:
                    if as_whole and ((i - m < 0 or not s[i - m].isalnum()) and (i + 1 >= n or not s[i + 1].isalnum())):
                        # print("doc num: ",docnum, "row num: " , rownum,"col no: ", colnum-m+1, "Pattern occcurs with shift as whole", i-m+1,text[i-m+1: i+5])
                        result_label = Label(output_frame,
                                            text=f"Doc num: {docnum} | Row num: {rownum} | Col num: {np.abs(colnum - m + 1)} | Pattern FOUND!",
                                            font=("Times New Roman", 14, "bold"),
                                            fg="white",
                                            # bg="#FFB6C1",
                                            bg=canvas_bg_color,
                                            #  padx=10, pady=10,
                                            relief="groove", borderwidth=5)
                        # )
                        # result_label.pack(pady=10)
                        result_label.grid(row=row_count,column=1,padx=10,pady=10)
                        row_count+=1
                        found_whole+=1
                    elif not as_whole:
                        # print("doc num: ",docnum, "row num: " , rownum,"col no: ", colnum-m+1, "Pattern occcurs with shift as substr", i-m+1,text[i-m+1: i+5])
                        result_label = Label(output_frame,
                                            text=f"Doc num: {docnum} | Row num: {rownum} | Col num: {np.abs(colnum - m + 1)} | Pattern FOUND!",
                                            font=("Times New Roman", 14, "bold"),
                                            fg="#8B008B",
                                            # bg="#FFB6C1",
                                            bg=canvas_bg_color,
                                            #  padx=10, pady=10,
                                            relief="groove", borderwidth=5)
                        # )
                        # result_label.pack(pady=10)
                        result_label.grid(row=row_count,column=2,padx=10,pady=10)
                        row_count+=1
                        found+=1
                        
                    q = prefix[q-1]
                colnum += 1
            end_time = time.time()
            print('found_whole', found_whole)
            print('found', found)
            # time_taken = end_time - start_time
            time_taken = end_time - start_time
            time_label = Label(output_frame, text=f"Time Taken, KMP: {np.abs(time_taken):.2f} seconds", font=("Times New Roman", 14, "bold"), fg="blue", bg="lightpink")
            time_label.grid(row=row_count + 1, column=1, padx=10, pady=10)
            return time_taken
        # first label of find what
        findwhat_label = Label(root,text="Find What: ",font=("Times New Roman", 30,"bold"),bg='lightpink')
        findwhat_label.grid(row=22, column=1, padx=25, pady=50)
        # now create a input entry text
        findwhat_entry = Entry(root, font=("Times New Roman", 20),bg='lightpink')  
        findwhat_entry.grid(row=22, column=2, padx=1,pady=45) 
        
        def get_text():
            findwhat = findwhat_entry.get()
            if not findwhat:  # Check for empty input
                error_label = Label(root, text="Error: Search input cannot be empty.", font=("Times New Roman", 14, "bold"), fg="red")
                error_label.grid(row=25, column=2, padx=10, pady=10)  # Display error message on the GUI
                return None
            return findwhat
        def show_value_1():
            print("Checkbox Value:", match_whole_word.get())  
        def show_value_2():
            print("Checkbox Value:", case_sensitive.get())
        findwhat = get_text()
        def clear_input():
            findwhat_entry.delete(0, END) # when clear button will be clicked we will empty the text written on # text box
            
        
        # cancel_button.pack()
        # checkbox for Match Whole Word Only
        match_whole_word = IntVar()
        match_case = IntVar()
        checkbox = Checkbutton(root, text="Match Whole Word Only", variable=match_whole_word, font=("Times New Roman", 20), bg='lightpink')
        checkbox.grid(row=23, column=2,pady=0)
        # for matching String Cases
        checkbox2 = Checkbutton(root, text="Match Case", variable=match_case, font=("Times New Roman", 20), bg='lightpink')
        checkbox2.grid(row=24,column=2,padx=20,pady=20)
            
        findwhat_button = tk.Button(root,text="Find Next", font=("Times New Roman", 20),bg='lightpink',highlightbackground="lightpink",highlightcolor="lightpink",highlightthickness=5,borderwidth=0,command=lambda: kmp_matcher(text, get_text(), match_whole_word.get(), match_case.get()) if get_text() else None )
        findwhat_button.grid(row=22, column=3, padx=2, pady=40)
        # next button of cancel
        # by pressing cancel we will automatically erase the content written in the text box
        cancel_button = tk.Button(root, text="Cancel", font=("Times New Roman", 20),bg='lightpink',highlightbackground="lightpink",highlightcolor="lightpink",highlightthickness=5,borderwidth=0,command=clear_input)         
        cancel_button.grid(row=22, column=4)
        root.mainloop()

    
    
    
def brute_gui(text):
            # create window
            
        root = tk.Tk()
        root.title("String Matching GUI")
        root.geometry("2000x2000")
        root.bg_image = PhotoImage(file="C:\\Users\\User\\Downloads\\PIC1.png")
        image = root.bg_image
        background_label = Label(root, image=root.bg_image)
        background_label.place(x=0, y=0,relheight=1) 
        output_frame = create_scrollable_frame(root)
        def Brute_Force(text, pat,case_sensitive=False, as_substr=True):
            
                start_time = time.time()
                found = 0
                row_count = 1
                found_whole= 0
                rownum= 1 
                colnum = 0
                docnum = 0
                m = len(pat)
                n = len(text)
                if not case_sensitive:
                    text = text.lower()
                    pat = pat.lower()
                for i in range(len(text)):
                    c = 0
                    if text[i] == '\n':
                        rownum += 1
                        colnum = 0
                    # if re.match(r"Research#[1-10]", text[i:i+10]):
                    if text[i] == '^':
                        docnum += 1
                        rownum, colnum = 1,0
                        continue
                    for j in range(len(pat)):
                        c+=1
                        if text[i+j] != pat[j]:
                            c = 0
                            break
                    if as_substr and c == m:
                        # print("doc num: ",docnum, "row num: " , rownum,"col no: ", colnum, " found at index: ", i, text[i:i+j+5])
                        result_label = Label(output_frame,
                                                text=f"Doc num: {docnum} | Row num: {rownum} | Col num: {np.abs(colnum - m + 1)} | Pattern FOUND!",
                                                font=("Times New Roman", 14, "bold"),
                                                fg="white",
                                                bg="lightpink",
                                                #  padx=10, pady=10,
                                                relief="groove", borderwidth=5)
                        # result_label.pack(pady=10)
                        result_label.grid(row=row_count,column=1)
                        row_count+=1
                        found+=1
                        
                    if i + m > n:
                            break
                    
                    if not as_substr and c == m and ((i == 0 or not text[i - 1].isalnum()) and (i + m >= n) or not text[i + len(pat)].isalnum()):
                        # print("doc num: ",docnum, "row num: " , rownum,"col no: ", colnum, "found whole at index: ",i, " ", text[i:i+j+5])
                        result_label = Label(output_frame,
                                                text=f"Doc num: {docnum} | Row num: {rownum} | Col num: {np.abs(colnum - m + 1)} | Pattern FOUND!",
                                                font=("Times New Roman", 14, "bold"),
                                                fg="white",
                                                bg="lightpink",
                                                #  padx=10, pady=10,
                                                relief="groove", borderwidth=5)
                        # result_label.pack(pady=10)
                        result_label.grid(row=row_count,column=1)
                        row_count+=1
                        
                        found_whole+=1
                    colnum+=1
                # end_time = time.time()
                print('found_whole',found_whole)
                print('found',found)  
                end_time = time.time()
                print('End time: ',end_time)
                print('Start time: ',start_time)
                time_taken = start_time - end_time
                result_label = Label(output_frame, text=f"Time Taken, Brute Force: {np.abs(time_taken):.2f} seconds", font=("Times New Roman", 14, "bold"), fg="blue", bg=canvas_bg_color)
                result_label.grid(row=row_count, column=1, padx=10, pady=10)    
                return time_taken
        # first label of find what
        findwhat_label = Label(root,text="Find What: ",font=("Times New Roman", 30,"bold"),bg='lightpink')
        findwhat_label.grid(row=22, column=1, padx=25, pady=50)
        # now create a input entry text
        findwhat_entry = Entry(root, font=("Times New Roman", 20),bg='lightpink')  
        findwhat_entry.grid(row=22, column=2, padx=1,pady=45) 
        
        def get_text():
            findwhat = findwhat_entry.get()
            return findwhat
        def show_value_1():
            print("Checkbox Value:", match_whole_word.get())  
        def show_value_2():
            print("Checkbox Value:", case_sensitive.get())
        findwhat = get_text()
        def clear_input():
            findwhat_entry.delete(0, END) # when clear button will be clicked we will empty the text written on # text box
            
        
        # cancel_button.pack()
        # checkbox for Match Whole Word Only
        match_whole_word = IntVar()
        match_case = IntVar()
        checkbox = Checkbutton(root, text="Match Whole Word Only", variable=match_whole_word, font=("Times New Roman", 20), bg='lightpink')
        checkbox.grid(row=23, column=2,pady=0)
        # for matching String Cases
        checkbox2 = Checkbutton(root, text="Match Case", variable=match_case, font=("Times New Roman", 20), bg='lightpink')
        checkbox2.grid(row=24,column=2,padx=20,pady=20)
            
        findwhat_button = tk.Button(root,text="Find Next", font=("Times New Roman", 20),bg='lightpink',highlightbackground="lightpink",highlightcolor="lightpink",highlightthickness=5,borderwidth=0,command=lambda: Brute_Force(text, get_text(), case_sensitive=match_case.get(), as_substr=match_whole_word.get()) if get_text() else None )
        findwhat_button.grid(row=22, column=3, padx=2, pady=40)
        # next button of cancel
        # by pressing cancel we will automatically erase the content written in the text box
        cancel_button = tk.Button(root, text="Cancel", font=("Times New Roman", 20),bg='lightpink',highlightbackground="lightpink",highlightcolor="lightpink",highlightthickness=5,borderwidth=0,command=clear_input)         
        cancel_button.grid(row=22, column=4)
        root.mainloop()
    


# making main function which runs everything
def main():
        
    # defining variable
    # root = tk.Tk()
    brute = False
    kmp = False
    chk1=False
    chk2=False
    findwhat = '\0'
    # get the whole text
    text = "" 
    try:
        for i in range(1,11):
            filename = "C:\\Users\\User\\Downloads\\Assignmnet three\\Assignmnet three\\" + "Research#" + str(i) + ".txt"
            with open(filename, 'r', encoding='utf-8') as file:
                text += "^" + file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode contents of {filename}. Invalid file format.")
    
    # now take input if the user wants kmp or brute
    usr_inp = input('Select Algorithm:\n 1) Brute Force \n 2) KMP \n')
    
    if usr_inp==2:
        # this will create gui for kmp
        kmp_gui(text)
        
    else:
        # this will create gui for brute force
        brute_gui(text)

        
        

main()
        
        
    