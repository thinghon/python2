print("20224016-박소호")
try:
    x=float(input("숫자 입력:"))
    inverse=1.0/x
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print("0으로 나눈 에로:" + str(e))
finally:
    print("예외가 발생하지 않거나 또는 발생할 수 있음.")
