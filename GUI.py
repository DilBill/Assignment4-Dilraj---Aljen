import tkinter as tk
from tkinter import ttk
from dataMangement import Manager
def find():
    val = entryFind.get()
    type = ""
    if option1.get() == 1:
        type = "Model"
    elif option2.get() == 1:
        type = "Vin"
    val2 = Manager.find(val,type)
    font = f"Car seleceted: {val2}"
    displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
    displayBox.insert(tk.INSERT,font)
    displayBox.place(x=325,y=75)
    print(val2, "Has been Found")
    return val2

def add():
    val = entryYear.get()
    val2 = entryMake.get()
    val3 = entryModel.get()
    val4 = entryVin.get()
    val5 = Manager.add(val, val2, val3, val4)
    font = f"Car seleceted: {val5}"
    displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
    displayBox.insert(tk.INSERT,font)
    displayBox.place(x=325,y=75)
    print(val5, "Has been Added")
    return val5

def update():
    val = entryFind.get()
    val2 = entryYear.get()
    val3 = entryMake.get()
    val4 = entryModel.get()
    val5 = entryVin.get()
    val6 = Manager.update(val2, val3, val4, val5,val)
    font = f"Car seleceted: {val6}"
    displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
    displayBox.insert(tk.INSERT,font)
    displayBox.place(x=325,y=75)
    print(val6, "Has been Added")
    return val6

def delete():
    val = entryFind.get()
    val2 = Manager.delete(val)
    font = f"Car seleceted: {val2}"
    displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
    displayBox.insert(tk.INSERT,font)
    displayBox.place(x=325,y=75)
    print(val, val2, "Has been Deleted")
    return val2

def showAll():
    val2 = Manager.showAll()
    font = f"{val2}"
    displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
    displayBox.insert(tk.INSERT,font)
    displayBox.place(x=325,y=75)
    print(val2)
    return val2
    

win = tk.Tk()
win.title("Car Garage")
win.geometry("700x500")

label = ttk.Label(win,text="My Car Garage\n")
label.place(x=300,y=10)
make = ttk.Label(win, text="Car Make")
make.place(x= 5, y=50)

# Set the default value for the ComboBox
entryMake = ttk.Entry(win)# Set the default value
entryMake.place(x=110,y=50)

year = ttk.Label(win, text="Year")
year.place(x=5,y=100)

# Set the default value for the ComboBox
entryYear = ttk.Entry(win)# Set the default value
entryYear.place(x=110,y=100)

vin = ttk.Label(win, text="Car Vin Number")
vin.place(x=5, y=150)

# Set the default value for the ComboBox
entryVin = ttk.Entry(win)# Set the default value
entryVin.place(x=110,y=150)

model = ttk.Label(win, text="Car model")
model.place(x= 5, y=200)

# Set the default value for the ComboBox
entryModel = ttk.Entry(win)# Set the default value
entryModel.place(x=110,y=200)

entryFind = ttk.Entry(win)
entryFind.place(x= 380, y=380)

addBtn = ttk.Button(win, text="Add Car", command=add)
addBtn.place(x=150,y=280)

updateBtn = ttk.Button(win,text="Update Car",command=update)
updateBtn.place(x=450, y=280)

deleteBtn = ttk.Button(win,text="Delete Car",command=delete)
deleteBtn.place(x=300,y=280)

findBtn = ttk.Button(win,text="Find Car",command=find)
findBtn.place(x= 275,y=380)

showBtn = ttk.Button(win,text="Show All",command=showAll)
showBtn.place(x=450,y=230)

option1 = tk.IntVar()

option2 = tk.IntVar()


checkBtn1 = tk.Checkbutton(win,text="By Model",variable=option1,onvalue=1,offvalue=0)
checkBtn1.place(x=350,y=340)

checkBtn2 = tk.Checkbutton(win,text="By Vin",variable=option2,onvalue=1,offvalue=0)
checkBtn2.place(x=450,y=340)

displayBox = tk.Text(win,bg="white",width=50,height=10,fg="black")
displayBox.place(x=325,y=75)

win.mainloop()




