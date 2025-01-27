n = int(input())
nums = list(map(int, input().split()))
add,sub,mul,div = map(int, input().split())

minimum = 1000000000
maximum = -1000000000
# 초기화

def dfs(i, now): # 사용한 연산자 개수, 현재 값
    global add, sub,mul,div, minimum, maximum
    if(i==n):
        minimum = min(minimum,now)
        maximum = max(maximum,now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+nums[i])
            # 다시 복구
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*nums[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/nums[i]))
            div += 1

dfs(1, nums[0])

print(maximum)
print(minimum)
