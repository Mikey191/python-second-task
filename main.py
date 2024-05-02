#простое число - это число которое делится на 1 и только на себя самого
for i in range(2, 100):
    flag = True
    for j in range(2, int(i/2) + 1):
        if (i % j) == 0:
            flag = False
            break
    if flag:
        print(i)