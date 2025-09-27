print("20224016-박소호")
scores = {}
result_f = open("C:\\Users\\박소호\\Documents\\프로그래밍1\\results.txt")

for line in result_f:
    (name,score)=line.split()
    scores[score]=name
result_f.close()

print("The top scores were:")
for each_score in sorted(scores.keys(),reverse=True):
    print('Sufer ' + scores[each_score]+' scored '+each_score)
