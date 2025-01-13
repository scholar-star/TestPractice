array=[('바나나',2),('사과',5),('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting) # 함수를 둠(함수 기준 반환) : 개별 원소에 대해 함수 적용
print(result)