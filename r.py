import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1 # count = count + 1
    ans = input('請猜一個數字: ')
    ans = int(ans)
    if ans == r:
        print('恭喜猜對！')
        print('這是你猜的第', count, '次')
        break
    else:
        if ans > r:
            print('太大了')
        else:
            print('太小了')
        print('這是你猜的第', count, '次')
