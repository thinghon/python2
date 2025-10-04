#채팅 서버 프로그램
from socket import*
from threading import*

#메시지 수신 함수(스레드)
def serverRecv():
    while True:
        #데이터 수신하고, 디코드하여 출력
        clientMsg = connectionSocket.recv(1024)
        print("[클라이언트]" + clientMsg.decode("utf8") + "\n")

#서버 네트워크 연결 초기화
print("서버 네트워크 연결 초기화....")

#호스트 주소 지정
serverProt = 9000

#서버 소켓 생성
serverSocket = socket(AF_INET, SOCK_STREAM)

#주소와 소켓 결합
serverSocket.bind(('', serverProt))

#연결 요청 청취
serverSocket.listen(1)

#연결 요청 수락, 연결 소켓 리턴
connectionSocket, addr = serverSocket.accept()
print("클라이언트 연결됨.....", addr, "\n")

#스레드 생성 및 실행
Thread(target = serverRecv).start()

#데이터 입력 및 송신 무한 루프
while True:
    #송신 데이터 입력
    msg = input()
    #문자열 인코드하여 데이터 송신
    connectionSocket.send(msg.encode("utf8"))

connectionSocket.close()