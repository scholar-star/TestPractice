d = [0]*100 # 메모이제이션(캐싱) 준비

def fibo(x):
    if x==1 or x==2:
        return 1

    if d[x]!=0: # 이미 계산되었다면
        return d[x]

    d[x] =fibo(x-1)+fibo(x-2) # 아직 계산이 안 되었으면
    return d[x]

# DP
print(fibo(99))