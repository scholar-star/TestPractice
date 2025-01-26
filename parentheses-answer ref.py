def solution(p):
    stack = []
    answer = ''
    if (p != ''):
        l = 0
        r = 0
        i = 0
        for s in range(len(p)):
            if (p[s] == '('):
                l += 1
            if (p[s] == ')'):
                r += 1
            if (l == r):
                i = s
                break
        u = p[:i + 1]
        if (i == len(p) - 1):
            v = ''
        else:
            v = p[i + 1:]
        print(u, v)

        right = True
        for ui in range(len(u)):
            if (u[ui] == '('):
                stack.append(u[ui])
            if (u[ui] == ')'):
                if (len(stack) == 0):
                    right = False
                    break
                else:
                    stack.pop(0)
        if (right): # 재귀를 사용
            answer = u + solution(v)  # V 결과를 붙여서 반환
        else:
            answer += '('
            answer += solution(v) # V 결과 붙이고
            answer += ')'
            u = list(u[1:len(u) - 1])  # iteration : list화(이게 없으면 iteration 안됨)
            print(u)
            for j in range(len(u)): #괄호 방향 반대로
                if (u[j] == '('):
                    u[j] = ')'
                else:  # 재변경 방지
                    u[j] = '('
            answer += ''.join(u)
            print(answer)
    return answer # 리턴은 분명히 존재(종료조건 존재)