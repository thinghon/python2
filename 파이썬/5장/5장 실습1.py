scores=[]
names=[]

result_f=("C:\\Users\\박소호\\Documents\\프로그래밍1\\results.txt")

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
