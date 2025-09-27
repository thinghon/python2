from tkinter import*
import tkinter.messagebox
from tkinter import filedialog as fd
from tkcalendar import Calendar
from datetime import *

total_price = 0 

#수입 내역을 수입파일에 적는 함수
def save_input_data(): 
    try:
        input_fileD=open("C:\\Users\pki10\\Desktop\\대학교\\1-1 프로그래밍1\\자료\\가계부\\가계부 수입.txt",'a')
        input_fileD.write("%s\n" %text_2.get('1.0',END)) #text칸에 있는 수입 내역 전체를 받아와 파일에 저장한다.
        btn_classification_input.set("분류") #옵션메뉴를 초기화한다.
        ent_input_2.delete(0,END) #수입내역중 금액을 적는 enter칸을 초기화한다
        text_2.delete('1.0',END) #수입내역을 띄우는 text칸을 초기화한다
    except Exception as ex: #파일에 내역을 쓸수없는경우 즉 예외사항 발동시 발동한다
        tkinter.messagebox.showerror("Error!","Can't write to the file\n %s"%ex) #해당내용이 뜨도록 에러창을 뛰운다

#지출 내역을 지출 파일에 적는 함수
def save_output_data(): 
    try:
        output_fileD=open("C:\\Users\\pki10\\Desktop\\대학교\\1-1 프로그래밍1\\자료\\가계부\\가계부 지출.txt",'a')
        output_fileD.write("%s\n" %text_1.get('1.0',END))
        btn_classification_output.set("분류")
        ent_output_2.delete(0,END)
        text_1.delete('1.0',END)
    except Exception as ex:
        tkinter.messagebox.showerror("Error!","Can't write to the file\n %s"%ex)

#총자산 변경 사항을 파일에 적는 함수
def save_money(): 
    global total_price
    money_fileD=open("C:\\Users\\pki10\\Desktop\\대학교\\1-1 프로그래밍1\\자료\\가계부\\자산.txt","a")
    money_fileD.write("총자산:"+str(total_price)+"원\n") #바뀐 자산을 파일에 적는다

#가계부에서 수입에 맞는 위젯들을 gui 뛰우는 함수
def show_input(): 
    btn_input.configure(bg="yellow") #btn_input(수입)버튼을 노랑색을 바꾼다
    btn_output.configure(bg="white") #tbn_output(지출)버튼을 하얀색을 바꾼다
    btn_money_change.configure(bg="white") #btn_money_change(자산변경)버튼을 하얀색으로 바꾼다
    frame3.pack_forget() #frame3번에 위치한 위젯들을 감춘다
    frame4.pack_forget() #frame4번에 위치한 위젯들을 감춘다
    frame6.pack_forget() #frame6번에 위치한 위젯들을 감춘다
    frame7.pack_forget() #frame7번에 위치한 위젯들을 감춘다
    """fill로 frame2에 사용되는공간을 사용되지 않는공간까지 늘린다.
    expand로 요구되지 않은공간도 요구된공간을 확장시킨다
    이로 인해 창의 크기가 변할때 프레임의 크기도 자동 조절된다""" 
    frame2.pack(fill="both", expand=True) 
    frame5.pack(fill="both", expand=True)

#지출 관련 위젯들 띄우기
def show_output():
    btn_input.configure(bg="white")
    btn_output.configure(bg="yellow")
    btn_money_change.configure(bg="white")
    frame5.pack_forget()
    frame7.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack(fill="both", expand=True)
    frame6.pack(fill="both", expand=True)

#총지출 버튼 관련 위젯들 띄우기
def show_money():
    btn_input.configure(bg="white")
    btn_output.configure(bg="white")
    btn_money_change.configure(bg="yellow")
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack(fill="both", expand=True)

#파일 오픈과 관련된 위젯 띄우기
def show_file():
    btn_input.configure(bg="white")
    btn_output.configure(bg="white")
    btn_money_change.configure(bg="white")
    frame5.pack_forget()
    frame6.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame7.pack(fill="both", expand=True)
    open_file()

#날짜 선택 달력
def show_cal(m): 
    new_window = Tk() #tkinter 애플리케이션 윈도우 생성
    new_window.title("달력") #윈도우 이름을 달력으로 설정
    new_window.geometry("300x300") #윈도우 크기 설정

    today_date=datetime.now() #현재 시간을 변수에 저장
    today_year=today_date.year #현재 시간에서 년도를 변수에 저장
    today_month=today_date.month #현재 시간에서 월을 변수에 저장
    today_day=today_date.day #현재 시간에서 일을 변수에 저장
    
    #달력을 현재 날짜를 기준으로 새로운 윈도우창에 띄운다
    cal = Calendar(new_window, selectmode = "day", year = today_year, month = today_month, day = today_day)
    cal.pack(pady = 20) #위아래 여백을 20둔다
    
    #수입 날짜 입력칸 날짜를 입력하는 함수
    def get_input_date():
        ent_input_cal.delete(0,END) #날짜 입력칸 내용을 전부 지운다
        ent_input_cal.insert(INSERT,cal.get_date()) #달력으로 선택한 날짜를 날짜 입력칸에 추가한다
        new_window.destroy() #새로운 윈도창을 닫는다
    
    #수출 날짜입력칸에 날짜를 입력하는 함수
    def get_output_date():
        ent_output_cal.delete(0,END)
        ent_output_cal.insert(INSERT,cal.get_date())
        new_window.destroy()

    if m == "input": #수입 버튼인지 지출버튼인지 구별한다
        Button(new_window, text = "Get Date", command = get_input_date).pack(pady = 20)
    elif m == "output":
        Button(new_window, text = "Get Date", command = get_output_date).pack(pady = 20)

#자산을 파일에서 가져온다.
def money():
    global total_price
    
    money_fileD=open("C:\\Users\\pki10\Desktop\\대학교\\1-1 프로그래밍1\\자료\\가계부\\자산.txt")
    money_txt = money_fileD.read()
    money_fileD.close()
    target_1 = "총자산:"
    target_2 = "원"
    gate_1 = 0
    gate_2 = 0
    rate_1 = []
    rate_2 = []

    """가계부의 특징상 기존의 자산 변경사항을 알수있도록 자산 변경 내역을 꾸준히 저장시켜
    겹치는 단어가 있다. 가장 최신 내역인 맨뒤에있는 자산만을 가져오기 위해 아래와 같이 했다."""
    while gate_1 > -1:
        gate_1 = money_txt.find(target_1,gate_1) #파일의 gate_1으로 부터 target_1의 위치를 찾는다.
        rate_1.append(gate_1) #리스트에 추가한다
        if gate_1 > -1: #파일 내용이 끝났는지 알수있게 해준다
            gate_1 += len(target_1) #target_1길이만큼 추가시켜 뒤에 있는 target_1을 찾게한다.
    while gate_2 > -1:
        gate_2 = money_txt.find(target_2,gate_2)
        rate_2.append(gate_2)
        if gate_2 > -1:
            gate_2 += len(target_2)
    rate_1.reverse() #맨뒤에있는 내용이 필요해 리스트를 거꾸로 한다
    rate_2.reverse()
    start_money=rate_1[1]+4
    end_money=rate_2[1]
    total_price=int(money_txt[start_money:end_money])

#자산을 변경하는 함수
def money_change():
    global total_price
    try:
        total_price = int(ent_money_1.get()) #자산변경 입력칸의 내용으로 자산을 변경한다.
    except Exception: #자산 변경칸에 숫자외에 다른것을 썻을때 오류창을 띄운다
        tkinter.messagebox.showerror("Error!","자산 변경칸에 숫자만을 입력해주세요!!")
    ent_money_1.delete(0,END) #자산 변경칸 내용을 지운다
    save_money() #변경된 자산을 저장한다
    print_money() #변경된 자산을 tkinter창에 띄운다

#자산을 tkinter창에 띄운다
def print_money():
    global total_price
    label_price.configure(text='총자산:'+str(total_price)+"원")

#text칸 내용을 전부 지운다
def delete_contend():
    text_3.delete('1.0',END)

#입력한 지출 내용을 text칸에 정리해서 띄운다
def print_output():
    global total_price
    tmp_output=""
    classification_output=str(btn_classification_output.get())
    try:
        money_output=int(ent_output_2.get())
    except Exception: #지출칸에 숫자외에 다른문자를 입력했을때 오류창을 띄운다
        tkinter.messagebox.showerror("Error!","지출칸에 숫자만 입력해주세요!!")
    tmp_output=str(ent_output_cal.get())+"\n"+classification_output+":"+str(money_output)+"원\n"
    total_price -= money_output #지출한만큼 자산에서 뺀다
    text_1.insert(INSERT,tmp_output)
    btn_classification_output.set("분류")
    ent_output_2.delete(0,END)
    ent_output_cal.delete(0,END)
    print_money()
    save_money()
 
#입력한 수입 내용을 text칸에 정리해서 띄운다
def print_input():
    global total_price
    tmp_input=""
    classification_input=str(btn_classification_input.get()) 
    try:
        money_input=int(ent_input_2.get())
    except Exception:
        tkinter.messagebox.showerror("Error!","지출칸에 숫자만 입력해주세요!!")
    tmp_input=str(ent_input_cal.get())+"\n"+classification_input +":"+str(money_input)+"원\n"
    total_price += money_input #수입만큼 자산을 증가시킨다
    text_2.insert(INSERT,tmp_input)
    btn_classification_input.set("분류")
    ent_input_2.delete(0,END)
    ent_input_cal.delete(0,END)
    print_money()
    save_money()

#가계부 내역 파일 오픈
def open_file():
    household_f=fd.askopenfile()
    household_contend=household_f.read()
    text_3.delete('1.0',END)
    text_3.insert(INSERT,household_contend) #가계부 내역을 text칸에 넣는다
    household_f.close()

money()

#기본 버튼
window = Tk() #tkinter 애플리케이션 윈도우 생성
window.title("가계부 프로그램") #윈도우 이름 설정
window.geometry("650x350+500+300") #윈도우 좌표와 크기 설정
window.resizable(False, False) #윈도우 창 크기를 고정시킨다

#윈도우창에 프레임으로 구역을 정한다
frame1 = Frame(window, width="600", height="10")
frame1.pack(fill="both")

frame2 = Frame(window, width="600")
frame2.pack(fill="both", expand=True)

frame3 = Frame(window, width="600")

frame4 = Frame(window, width="600")

frame5 = Frame(window, width="600")
frame5.pack(fill="both", expand=True)

frame6 = Frame(window, width="600")

frame7 = Frame(window, pady="30", width="600")

#지출,수입,자산변경과 같은 파트를 나누는 버튼
btn_input = Button(frame1, text="지출", padx="10", pady="10", bg="yellow", command=show_input)
btn_input.grid(row=0, column=0, padx=10, pady=10)

btn_output = Button(frame1, text="수입", padx="10", pady="10", bg="white", command=show_output)
btn_output.grid(row=0, column=1, padx=10, pady=10)

btn_money_change = Button(frame1, text="자산 변경", padx="10", pady="10", bg="white", command=show_money)
btn_money_change.grid(row=0, column=2, padx=10, pady=10)

label_price = Label(frame1, text="총자산:"+str(total_price)+"원", width="20",padx="5", pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column=3, padx=0, pady=10)

# 지출
ent_output_cal=Entry(frame2, width=11)
ent_output_cal.grid(row=1, column=0, padx=10)

btn_output_cln=Button(frame2,text="날짜",command=lambda:show_cal("output"))
btn_output_cln.grid(row=0, column=0)

btn_classification_output=StringVar()
btn_classification_output.set("분류")
options=["식비","교통/차량","문화생활","마트/편의점","패션/미용","생활용품","주거/통신","건강","교육","경조사/회비","부모님","기타"]
btn_output_1=OptionMenu(frame2,btn_classification_output,*options)
btn_output_1.grid(row=0, column=1, pady=10)

lbel_output_1=Label(frame2,text="금액:")
lbel_output_1.grid(row=0, column=2)

ent_output_2=Entry(frame2)
ent_output_2.grid(row=0, column=3)

lbel_output_2=Label(frame2,text="(원)")
lbel_output_2.grid(row=0, column=4)

btn_output_end = Button(frame2, text="내용 출력", padx="10", pady="10", command=print_output)
btn_output_end.grid(row=0, column=5, padx=10, pady=10)

# 수입
ent_input_cal=Entry(frame3, width=11)
ent_input_cal.grid(row=1, column=0, padx=10)

btn_input_cln=Button(frame3, text="날짜",command=lambda:show_cal("input"))
btn_input_cln.grid(row=0, column=0)

btn_classification_input=StringVar()
btn_classification_input.set("분류")
options=["월급","부수입","용돈","상여","금융소득","기타"]
btn_input_1=OptionMenu(frame3,btn_classification_input,*options)
btn_input_1.grid(row=0, column=1, pady=10)

lbel_input_1=Label(frame3,text="금액:")
lbel_input_1.grid(row=0, column=2)

ent_input_2=Entry(frame3)
ent_input_2.grid(row=0, column=3)

lbel_input_2=Label(frame3,text="(원)")
lbel_input_2.grid(row=0, column=4)

btn_input_end = Button(frame3, text="내용 출력", padx="10", pady="10", command=print_input)
btn_input_end.grid(row=0, column=5, padx=10, pady=10)

#자산 변경
lbel_money_1=Label(frame4,text="총자산 변경:")
lbel_money_1.grid(row=0, column=1)

ent_money_1=Entry(frame4)
ent_money_1.grid(row=0, column=2)

lbel_input_2=Label(frame4,text="(원)")
lbel_input_2.grid(row=0, column=3)

btn_money = Button(frame4, text="자산 변경", padx="10", pady="10", command=money_change)
btn_money.grid(row=0, column=4, padx=10, pady=10)

#가계부 파일 오픈
btn_file_open=Button(frame1,text='파일오픈', padx="10", pady="10", width="10", bg="white",command=show_file).place(x=530,y=10)

btn_contend_delete=Button(window,text="내용삭제", padx="10", pady="10", width="10",command=delete_contend).place(x=530,y=75)

#내역 리스트
Label(frame5,text="지출 내용").pack()
text_1 = Text(frame5, height="10")
text_1.pack()
Button(frame5,text="Save",command=save_output_data).pack()

Label(frame6,text="수입 내용").pack()
text_2 = Text(frame6, height="10")
text_2.pack()
Button(frame6,text="Save",command=save_input_data).pack()

text_3 = Text(frame7, height="15")
text_3.pack(side=BOTTOM)

window.mainloop()