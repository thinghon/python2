print("20224016-박소호")
scores=[]
result_f=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\results.txt")
for line in result_f:
    (name,score)=line.split()
    scores.append(float(score))
result_f.close()

scores.sort()
scores.reverse()

print(scores[0])
print(scores[1])
print(scores[2])