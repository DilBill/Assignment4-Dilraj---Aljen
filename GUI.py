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

# Set the default value for the ComboBox
entryBox4 = ttk.Entry(win)# Set the default value
entryBox4.place(x=110,y=200)

entryBox5 = ttk.Entry(win)
entryBox5.place(x= 380, y=380)

addBtn = ttk.Button(win, text="Add Car", command=action)
addBtn.place(x=150,y=280)

updateBtn = ttk.Button(win,text="Update Car",command=action)
updateBtn.place(x=450, y=280)

deleteBtn = ttk.Button(win,text="Delete Car",command=action)
deleteBtn.place(x=300,y=280)

findBtn = ttk.Button(win,text="Find Car",command=action)
findBtn.place(x= 275,y=380)

showBtn = ttk.Button(win,text="Show All",command=action)
showBtn.place(x=450,y=230)

option = tk.IntVar

radioBtn1 = ttk.Radiobutton(win,text="By Model",variable= option,value=1)
radioBtn1.place(x=350,y=340)

radioBtn2 = ttk.Radiobutton(win,text="By Vin",variable=option,value=2)
radioBtn2.place(x=450,y=340)

displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
displayBox.place(x=325,y=75)

win.mainloop()




