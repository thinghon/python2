print("20224016-박소호")
scores=[]
names=[]
result_f=open("C:\\Users\\박소호\\Documents\\프로그래밍1\\results.txt")

for line in result_f:
    (name,score)=line.split()
    scores.append(float(score))
    names.append(name)
result_f.close()

scores.sort()
scores.reverse()
names.sort()
names.reverse()

print("The highest scores were:")
print(names[0]+'with'+str(scores[0]))
print(names[1]+'with'+str(scores[1]))
print(names[2]+'with'+str(scores[2]))
