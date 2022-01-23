# Programmers - Level1 - 시저 암호

'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. 
"z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
'''

def solution(s, n):
    ans = ''
    res = 0
    result = 0
    
    for i in range(len(s)):
        if ord(s[i]) != 32:
            res = ord(s[i])
            if 97<= res <=122:
                result = res + int(n)
                if result > 122:
                    result = result - 26
            elif 65<= res <=90:
                result = res + int(n)
                if result >90:
                    result = result - 26
        else:
            result = ord(s[i])

        ans = ans + chr(result)
    return ans