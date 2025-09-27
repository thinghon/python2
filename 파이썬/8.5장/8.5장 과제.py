print("20224016-박소호")
import tkinter as tk
from tkinter import*
import tkinter.messagebox
from tkinter import filedialog as fd

def save_data():
    try:
        fileD=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\household.txt",'a')
        fileD.write("지출\n")
        fileD.write("%s\n" %contend.get('1.0',END))
        classification.set(None)
        money.delete(0,END)
        contend.delete('1.0',END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!","Can't write to the file\n %s"%ex)
    
def read_classification(file):
    classifications=[]
    classifications_f=open(file,encoding="utf-8")
    for line in classifications_f:
        classifications.append(line.rstrip())
    return classifications

def print():
    tmp=""
    classification_p=str(classification.get())
    try:
        money_p=int(money.get())
    except Exception:
        tkinter.messagebox.showerror("Error!","지출칸에 숫자만 입력해주세요!!")
    tmp= classification_p +":"+str(money_p)+"원\n"
    contend.insert(tk.INSERT,tmp)
    classification.set(None)
    money.delete(0,END)

app=Tk()
app.title('Head-ex Deliveries')
Label(app,text='분류:').pack()
classification=StringVar()
classification.set("분류")
options=read_classification("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\classification.txt")
OptionMenu(app,classification,*options).pack()

Label(app,text='지출:').pack()
money=Entry(app)
money.pack()
Button(app,text='출력',command=print).pack()
Label(app,text='내용:').pack()
contend=Text(app)
contend.pack()

Button(app,text="Save",command=save_data).pack()
app.mainloop()