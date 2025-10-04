#채팅 클라이언트 프로그램
from socket import*
from threading import*

#메서드 수신 함수(스레드)
def clientRecv():
    while True:
        #데이터 수신하고, 디코드하여 출력
        serverMsg = clientSocket.recv(1024)
        print("[서버]" + serverMsg.decode("utf8")+"\n")
    clientSocket.close()

#클라이언트 네트워크 연결 초기화
print("클라이언트 네트워크 연결 초기화.....")

#연결할 서버 주소 지정
serverName = '192.168.0.117'
servePort = 9000

#클라이언트 소켓 생성
clientSocket = socket(AF_INET,SOCK_STREAM)

#서버에 연결 요청
clientSocket.connect((serverName, servePort))
print("서버 연결됨...\n")

#스레드 생성 및 실행
Thread(target=clientRecv).start()

#데이터 입력 및 송신 무한 루프
while True:
    #송신 데이터 입력
    msg = input()
    #문자열 인코드하여 데이터 송신
    clientSocket.send(msg.encode("utf8"))

clientSocket.close()