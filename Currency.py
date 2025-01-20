n = int(input())
l = list(map(int, input().split()))

l.sort(reverse=True)
for i in range(1, 1000001):
    num = i
    for j in l:
        if(num<j):
            continue
        else:
            num -= j


    if(num==0):
        continue
    else:
        print(i)
        break
