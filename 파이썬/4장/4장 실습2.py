text = """
20224016-박소호
Soonchunhyang University
Department of Computer Science and Engineering
"""
f=open("C:/Users/박소호/Documents/프로그래밍1/test.txt",'w')
f.write(text)
f.close()

f = open('C:/Users/박소호/Documents/프로그래밍1/test.txt')
lines = f.read()
print(lines.upper())
