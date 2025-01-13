from time import time

array = [i for i in range(1,10001)]

start = time()

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 한 칸씩 밀어내고 이동하며 자리를 찾는 형식(삽입)
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

end = time()

print("Insert Sorting: {}".format(float(end-start)))