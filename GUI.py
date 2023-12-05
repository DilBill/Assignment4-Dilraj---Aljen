import tkinter as tk
from tkinter import ttk

def action():
    val = entryBox.get()
    val2 = entryBox2.get()
    val3 = entryBox3.get()
    val4 = entryBox4.get()
    font = f"Car seleceted: {val2} {val} {val4} {val3}"
    displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
    displayBox.insert(tk.INSERT,font)
    displayBox.place(x=325,y=75)
    print(val, val2, val3,val4,"Has been Added")
    return val,val2,val3,val4

win = tk.Tk()
win.title("Car Garage")
win.geometry("700x500")

label = ttk.Label(win,text="My Car Garage\n")
label.place(x=300,y=10)
label1 = ttk.Label(win, text="Select Car Make")
label1.place(x= 5, y=50)

# Set the default value for the ComboBox
entryBox = ttk.Entry(win)# Set the default value
entryBox.place(x=110,y=50)

label2 = ttk.Label(win, text="Select Year")
label2.place(x=5,y=100)

# Set the default value for the ComboBox
entryBox2 = ttk.Entry(win)# Set the default value
entryBox2.place(x=110,y=100)

label3 = ttk.Label(win, text="Car Vin Number")
label3.place(x=5, y=150)

# Set the default value for the ComboBox
entryBox3 = ttk.Entry(win)# Set the default value
entryBox3.place(x=110,y=150)

label4 = ttk.Label(win, text="Car model")
label4.place(x= 5, y=200)


win.mainloop()




