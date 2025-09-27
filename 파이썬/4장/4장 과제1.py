print("20224016-박소호")
scores =[]
result_f = open("C:\\Users\\박소호\\Documents\\프로그래밍1\\results.txt")
for line in result_f:
    (name,score)=line.split()
    scores.append(float(score))
result_f.close()

scores.sort()
file = open("C:\\Users\\박소호\\Documents\\프로그래밍1\\results.txt",'a')
a=0
for i in range(3):
    tes = str(scores[a])
    file.write("\n%s"%tes)
    a=a+1
file.close()

file = open("C:\\Users\\박소호\\Documents\\프로그래밍1\\results.txt",'r')
data = file.read()
print(data)
file.close
