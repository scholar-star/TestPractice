# 피보나치를 재귀함수로 표현
def fibo(x):
    if x==1 or x==2: # 두 번째 수이거나 첫 번재 수일때
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))
