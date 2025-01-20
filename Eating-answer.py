import heapq

from lxml.parser import result


# 떠올린 아이디어는 정답과 유사했지만, 구현을 하지 못함
# 우선순위 큐를 이용하면 구현하기 쉽다
def solution(food_times, k):
    if sum(food_times)<k:
        return -1

    # 우선순위 큐
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i],i+1)) # (음식 시간, 번호)의 튜플 형태로 삽입
        # 적은 순대로 정렬(오름차순)

    sum_value = 0 # 먹기 위해 사용한 누적시간
    previous = 0 # 이전 음식 소요 시간
    length = len(food_times) # 남은 음식 개수(떨어진 음식 개수는 신경 안 쓰고 움직일 것이므로)
    # 순회하면서 음식을 먹을 것이기에, 남은 음식수도 고려했어야 한다.
    # 즉, 한 음식을 다 소진하는 데 드는 시간은 length * 현재 음식 시간

    while sum_value + ((q[0][0] - previous)*length) <= k:
        now = heapq.heappop(q)[0] # 음식 소진 시간
        sum_value += (now-previous)*length # 현재까지의 누적합
        length -= 1 # 음식 하나를 다 먹었으므로 제외시킴
        previous = now # 이전 음식 시간

    result = sorted(q, key=lambda x: x[1]) # 음식 번호순대로 나열
    return result[(k-sum_value)%length][1] # k초 - 지금까지 먹은 시간
    # 순회하므로 현재 길이로 나눈 나머지를 index로 구함.

