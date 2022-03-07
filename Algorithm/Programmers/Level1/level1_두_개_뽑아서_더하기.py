# Programmers - Level1 - 두 개 뽑아서 더하기

'''
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
'''

#1

def solution(numbers):
    sum = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            sum.append(numbers[i]+numbers[j])
    answer = sorted(list(set(sum)))
    return answer


'''
#2

import itertools

def solution(numbers):
    num = list(itertools.combinations(numbers, 2))
    
    result = []
    for a, b  in num:
        result.append(a + b)
    
    result = list(set(result))
    answer = sorted(result)
    return answer
'''