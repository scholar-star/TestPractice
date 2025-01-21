def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        st = ""
        prev = s[:i] # 앞에서부터 i만큼 문자열 추출
        count = 1

        for j in range(i, len(s), i):
            if prev==s[j:j+i]: # 현재 문자열 == i이후 문자열(연속 동일)
                count += 1
            else:
                if(count>=2): # 연속 동일 X
                    st += str(count)+prev
                else:
                    st += prev
                prev = s[j:j+i] # 초기화
                count = 1

        if(count>=2):
            st += str(count)+prev
        else:
            st += prev
        answer = min(len(st), answer)
    return answer

print(solution("aabbACCC"))