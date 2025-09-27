print("20224016-박소호")
import random

print("축구 승부차기 게임")
print("당신은 골기퍼가 되어 날아오는 축구공을 막으십시오!")
print("게임방법: 왼쪽 또는 오른쪽 중 하나를선택해주세요!!")
n = 1
def game(n):
    success = 0
    while n <= 5:
        save = random.choice(['왼','오'])
        keeper = input("왼/오:")
        if save == keeper:
            print("성공!!")
            n = n+1
            success = success+1
        else:
            print('실패!!')
            n = n+1
    print('총 막은 횟수:%d번'%success)
game(n)
