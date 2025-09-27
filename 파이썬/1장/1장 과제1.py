print("20224016-박소호")

number = 0
even = 0
odd = 0
while number <= 100:
    if number % 2 == 0: 
       even = even + number
    else: 
        odd = odd + number
    number = number + 1
print("짝수:",even)
print("홀수:",odd)
