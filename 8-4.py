d = [0]*100

d[1]=1
d[2]=2
n=99

for i in range(3,n+1): # 반복적으로 작은 수에서 쌓아간다.
    d[i] = d[i-1]+d[i-2]

print(d[n])