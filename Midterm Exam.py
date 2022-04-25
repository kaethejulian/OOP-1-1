from tkinter import *
window = Tk()

window.geometry("500x400")
window.title("Midterm in OOP")

lbl= Label(window, text="Enter your fullname", font=12, fg="red")
lbl.place(x=40, y=80)

txtfld = Entry(window, bd = 3, font = ("Times New Roman",12))
txtfld.place(x=250, y=80)
txtfld2 = Entry(window, bd = 3, font = ("Times New Roman",12))
txtfld2.place(x=250, y=150)

def clicked():
    value=txtfld.get()
    txtfld2.insert(END,str(value))
btn =Button(window, text="Click to display your Fullname:", fg="red", command=clicked)
btn.place(x=40, y=150)

window.mainloop()