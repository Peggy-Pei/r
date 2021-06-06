import random

r = random.randint(1, 100)

while True:
    ans = input('請猜一個數字: ')
    ans = int(ans)
    if ans == r:
        print('恭喜猜對！')
        break
    else:
        if ans > r:
            print('太大了')
        else:
            print('太小了')
