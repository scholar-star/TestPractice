n,m,k = tuple(map(int, input().split()))
data = list(map(int, input().split()))
data.sort()
total = (m//(k+1))*(data[len(data)-1]*k+data[len(data)-2]*1) + (m%(k+1))*data[len(data)-1]
print(total)