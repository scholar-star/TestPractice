n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if(str(i).count('3')!=0 or str(j).count('3')!=0 or str(k).count('3')!=0):
                count += 1

print(count)