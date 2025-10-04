### TCP 클라이언트프로그램 
from socket import *
# 네트워크 TCP 연결초기화 
print("클라이언트TCP 초기화...") 
# 연결할서버주소젅정 
serverName = '192.168.0.39'
serverPort = 7000 
# 클라이언트소켓생성 
clientSocket = socket(AF_INET, SOCK_STREAM) 
# 서버에연결요청 
clientSocket.connect((serverName, serverPort)) 
print("서버연결됨 ...")
rawData = input('입력영문자: ')
 # 문잋열인코드하여데이터송신 
clientSocket.send(rawData.encode("utf8")) 
 # 데이터수신 
modifiedStr = clientSocket.recv(1024) 
print("서버로부터수신: " , modifiedStr.decode("utf8"))