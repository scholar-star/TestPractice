n,k = tuple(map(int, input().split()))
pro_count = 0

while(n!=1):
    if(n%k!=0):
        n -= 1
    else:
        n = n//k
    pro_count +=1

print(pro_count)
