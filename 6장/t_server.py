from socket import *
 # 네트워크 TCP 연결초기화 
print("서버 TCP 초기화 ...") 
serverPort = 7000 
 # 서버소켓생성 
serverSocket = socket(AF_INET, SOCK_STREAM) 
 # 주소와소켓결합 
serverSocket.bind(('', serverPort)) 
 # 연결요청청취 
serverSocket.listen(1)
while True: 
    # 연결요청수락, 연결소켓리턴 
    connectionSocket, addr = serverSocket.accept()
    print("클라이언트연결됨 ...", addr) 
    # 데이터수신 
    rawData = connectionSocket.recv(1024) 
    print("수신데이터: ", rawData.decode("utf8")) 
    # 대문잋변환 
    upperStr = rawData.upper() # 데이터송신 
    connectionSocket.send(upperStr)
    connectionSocket.close()