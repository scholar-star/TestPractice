import random
from datetime import datetime

start = datetime.now()# datetime

array = [i for i in range(1,10001)]
random.shuffle(array) # void

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

end = datetime.now()

print(end-start)