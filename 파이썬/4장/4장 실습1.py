print("20224016-박소호")
highest_score = 0
result_f = open("C:/Users/박소호/Documents/프로그래밍1/results.txt",'r')

for line in result_f:
    (name,score) = line.split()
    if float(score) > highest_score:
        highest_score = float(score)

result_f.close()
print("The highest scores was:")
print(highest_score)
