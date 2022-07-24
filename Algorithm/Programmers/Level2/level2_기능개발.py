# Programmers - Level2 - 기능개발

'''
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
'''


import math                                     # 올림함수를 위한 math 모듈 import


def solution(progresses, speeds):
    result = []                                         # 날짜 계산을 위한 result 리스트 생성
    for i in range(len(progresses)):
        temp = (100 - progresses[i]) / speeds[i]        # 남은 날짜에서 속도를 나눈 값을 temp에 저장
        result.append(math.ceil(temp))                  # temp값을 올림하여 result 리스트에 추가

    answer = []                                         # 결과값 저장을 위한 answer 리스트 생성
    cnt = 1                                             # cnt 변수 생성 후 1로 초기화
    flag = result[0]                                    # flag 변수 생성 후 result[0]으로 초기화
    for j in range(1, len(result)):
        if flag < result[j]:                            # result[j]가 flag보다 클 경우
            answer.append(cnt)                          # answer 리스트에 추가 후
            cnt = 1                                     # cnt 1로 초기화
            flag = result[j]                            # flag를 result[j]로 초기화
        else:                                           # 작거나 같을 경우
            cnt += 1                                    # cnt에 1을 더함

    answer.append(cnt)                                  # 마지막 cnt를 answer에 추가 후
    return answer                                       # answer 리턴