print("20224016-박소호")
def sum(n):
    if(n==1):
        return 1
    else:
        return sum(n-1)+n
print('---sum(10)')
print(sum(10))

print("---sum(100)")
print(sum(100))
