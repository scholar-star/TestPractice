# recursive binary
def binary_search(array, target, start, end):
    if start > end: # start지점과 end지점이 엇갈린다면
        return None # 종료조건

    mid = (start+end)//2
    # 소수점 이하를 버린다.(중간점)

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, len(array)-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1,"번째")
