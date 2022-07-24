# Programmers - Level1 - 폰켓몬

'''
N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어질 때,
N/2마리의 폰켓몬을 선택하는 방법 중,
가장 많은 종류의 폰켓몬을 선택하는 방법을 찾아,
그때의 폰켓몬 종류 번호의 개수를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(nums):
    answer = len(nums) // 2     # answer의 초기값으로 len(nums) // 2 를 대입
    nums_set = len(set(nums))   # nums_set의 초기값으로 중복값 제거한 nums 리스트 길이를 대입
    return nums_set if answer > nums_set else answer    # 만약 nums_set의 값이 answer보다 작다면 nums_set을 리턴
