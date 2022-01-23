# Programmers - Level1 - 소수 만들기

'''
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
'''

import math
def solution(nums):
    ans = []
    ans2 = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                ans.append(nums[i]+nums[j]+nums[k])
    ans.sort()
    for i in range(len(ans)):
        for j in range(2,int(math.sqrt(ans[i])+1)):
            if ans[i]%j==0:
                ans2.append(ans[i])
                break
    answer = len(ans) - len(ans2)
    return answer