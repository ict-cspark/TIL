def solution(s):
    answer = []
    s = s[1:-1]
    tp = []
    print(s)
    for i in s:
        if i == '{':
            temp = []
            t = ''
        elif i == ',':
            if t:
                temp.append(int(t))
        elif i == '}':
            tp.append(temp)
            t = ''
        else:
            t += i

    tp.sort(key=len)
    print(tp)
    return answer



x = solution("{{20,111},{111}}")
print(x)