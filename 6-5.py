array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    # tail : 피벗을 제외한 나머지 부분

    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x > pivot]
    # 분할을 list 안 비교 연산과 함께 수행

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))