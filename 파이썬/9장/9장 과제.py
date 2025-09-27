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
        classification.set("분류")  #옵션메뉴 초기화
        money.delete(0,END) #입력창 초기화
        contend.delete('1.0',END) #내용창 초기화
    except Exception as ex:
        tkinter.messagebox.showerror("Error!","Can't write to the file\n %s"%ex)
    
def read_classification(file):  
    classifications=[]
    classifications_f=open(file,encoding="utf-8") #메모장파일을 연다
    for line in classifications_f: #메모장파일을 line에 넣는다.
        classifications.append(line.rstrip()) #line을 줄단위로 나눈다
    return classifications

def print():
    tmp=""
    classification_p=str(classification.get())
    try:
        money_p=int(money.get())
    except Exception:  #int즉 money.get()이 숫자가 아닐때 발동한다 
        tkinter.messagebox.showerror("Error!","지출칸에 숫자만 입력해주세요!!")
    tmp= classification_p +":"+str(money_p)+"원\n" 
    contend.insert(tk.INSERT,tmp) #text칸에 tmp 변수를 넣는다
    classification.set(None) 
    money.delete(0,END)

def open_file():
    household_f=fd.askopenfile()
    household_contend=household_f.read()
    contend.insert(tk.INSERT,household_contend) #text칸안에 household 텍스트파일 내용을 넣는다
    household_f.close()

def delete_contend():
    contend.delete('1.0',END) #text칸을 초기화한다
    
app=Tk()
app.title('가계부')  # 제목표시줄을 가계부로한다
Label(app,text='분류:').pack()
classification=StringVar()
classification.set("분류")

options=read_classification("C:\\Users\\박소호\\Documents\\프로그래밍1\\자료\\가계부\\분류_지출.txt")
OptionMenu(app,classification,*options).pack() #classification 변수를 넣은 옵션메뉴를 만든다

Label(app,text='지출 금액:(원)').pack()
money=Entry(app)
money.pack()
Button(app,text='출력',command=print).pack()
Label(app,text='내용:').pack()
contend=Text(app)
contend.pack()

file_open=Button(app,text='파일오픈',command=open_file).place(x=50,y=50) #파일 오픈 버튼을 지정한 장소에 만든다
contend_delete=Button(app,text="내용삭제",command=delete_contend).place(x=130,y=50) #내용삭제 버튼을 지정한 장소에 만든다

Button(app,text="Save",command=save_data).pack()
app.mainloop()
