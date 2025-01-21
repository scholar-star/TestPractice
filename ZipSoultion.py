def solution(s):
    lens = []

    for i in range(1, (len(s) // 2) + 1):
        last = 0
        words = []
        st = ""
        for j in range(0, len(s) - (i - 1), i):
            words.append(s[j:j + i])
            last = j + i

        if (last <= len(s) - 1):
            words.append(s[last:])

        print(words)
        print(i)

        count = 1
        for k in range(0, len(words) - 1):
            if (words[k] == words[k + 1]):
                count += 1
            else:
                if (count == 1):
                    st += words[k]
                else:
                    st += str(count) + words[k]
                count = 1

            if (k == len(words) - 2):
                if (words[k] == words[k + 1]):
                    st += str(count) + words[k + 1]
                else:
                    st += words[k + 1]
                print(st)

        lens.append(len(st))
    return min(lens)

print(solution("aabbaccc"))
print(solution("abcabcdede"))

# runtime error