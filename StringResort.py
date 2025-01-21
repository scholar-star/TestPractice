s = [i for i in input()]

s.sort()

alpha_index = 0
for i in range(len(s)):
    if(s[i].isalpha()):
        alpha_index = i
        break

if(alpha_index == 0):
    if(s[0].isalpha()):
        print(''.join(s))
    else:
        print(str(sum(s)))
else:
    alphas = s[alpha_index:]
    total = sum([int(i) for i in s[:alpha_index]])
    new = ''.join(alphas)+str(total)
    print(new)
