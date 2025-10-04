import sqlite3
from flask import Flask, render_template, request
#20224016 박소호
app = Flask(__name__)

#순천향 서핑 대회 로그인 폼 렌더링
@app.route('/')
def surf():
    return render_template('loginForm.html')

#로그인 처리
@app.route('/login', methods=['POST']) 
def login():
    #폼 입력값 가져오기
    idn = request.form['id']
    pwd = request.form['passwd']

    #데이터베이스 연결
    conn = sqlite3.connect("member.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    #계정 id레코드 읽기
    cursor.execute('select * from meminfo where id = ?', (idn,)) 
    row = cursor.fetchone() 
    conn.close()

    #계정/비번 조사
    if row != None: 
        if idn == row['id'] and pwd == row['passwd']: 
            return render_template('surfForm.html')
        
        return("<h2>로그인에러 !!</h2>")


#회원가입 폼 렌더링
@app.route('/member', methods=['POST'])
def member():
    return render_template('memForm.html')

#회원가입 처리
@app.route('/register', methods=['POST']) 
def register():
    import datetime
    
    #폼 입력값 가져오기
    idn = request.form['id'] 
    pwd = request.form['passwd'] 
    na = request.form['name']
    #회원 등록 시간
    tm = datetime.datetime.now()
    
    #데이터베이스 연결
    conn = sqlite3.connect('member.db') 
    cursor = conn.cursor()

    #데이터베이스 등록
    cursor.execute(''' insert into meminfo (id, passwd, name, time) values(?, ?, ?, ?)''', (idn, pwd, na, tm))
    conn.commit()
    conn.close()

    mstr = "id = %s, passwd = %s, name = %s, time = %s" % (idn, pwd, na, tm) 
    outstr = "<h3>회원가입이되었습니다.</h3><hr><p>" + mstr

    return outstr

#선수 조회 처리
@app.route('/show', methods=['POST']) 
def show():
    #폼 입력값 가져오기
    na = request.form['name']

    #데이터베이스 연결 및 조회
    conn = sqlite3.connect('SoonSurf.db') 
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor() 
    cursor.execute(''' select * from surfinfo where name = ? ''', (na,)) 
    row = cursor.fetchone()
    conn.close()

    outstr = "<h2>선수조회</h2><br><hr>" 

    if row != None: 
        outstr += "name: %s <br>" % row['name'] 
        outstr += "score: %s <br>" % row['score'] 
        outstr += "gender: %s <br>" % row['gender'] 
        outstr += "country: %s <br>" % row['country']
    else: 
        outstr += "선수데이터가없습니다!!"

    return outstr

#선수 입력 처리
@app.route('/insert', methods=['POST']) 
def insert():
    #폼 입력값 가져오기
    na = request.form['name'] 
    sc = request.form['score'] 
    gn = request.form['gender'] 
    ct = request.form['country']
    
    #데이터베이스 삽입
    conn = sqlite3.connect('SoonSurf.db')
    cursor = conn.cursor()
    cursor.execute(''' insert into surfinfo 
    (name, score, gender, country) 
    values(?, ?, ?, ?)''', (na, float(sc), gn, ct))
    conn.commit()
    conn.close()
    outstr = "<h2>선수입력</h2><br><hr>"
    outstr += "name: %s <br>" % na 
    outstr += "score: %s <br>" % sc 
    outstr += "gender: %s <br>" % gn 
    outstr += "country: %s <br>" % ct

    return outstr
if __name__ == '__main__':
    app.run(host="192.168.0.96", port = "5000")