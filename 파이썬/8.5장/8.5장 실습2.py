print("20224016-박소호")
from tkinter import*
import tkinter.messagebox
def save_data():
    try:
        fileD=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\deliveries.txt",'a')
        fileD.write("Depot:\n")
        fileD.write("%s\n"%depot.get())
        fileD.write("Description:\n")
        fileD.write("%s\n" %description.get())
        fileD.write("Address:\n")
        fileD.write("%s\n" %address.get('1.0',END))
        depot.set(NONE)
        description.delete(0,END)
        address.delete("1.0",END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!","Can't write to the file\n %s"%ex)

def read_depots(file):
    depots=[]
    depots_f=open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

app=Tk()
app.title("Head-Ex Deliveries")

Label(app,text="Depot:").pack()
depot=StringVar()
depot.set(NONE)
options=read_depots("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\depots.txt")
OptionMenu(app,depot,*options).pack()

Label(app, text="Descripition:").pack()
description=Entry(app)
description.pack()

Label(app, text="Address:").pack()
address=Text(app)
address.pack()

Button(app,text="Save",command=save_data).pack()
app.mainloop()
