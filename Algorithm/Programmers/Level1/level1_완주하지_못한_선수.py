# Programmers - Level1 - 완주하지 못한 선수

'''
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
'''

def solution(participant, completion):

    participant.sort()      # 오름차순으로 정렬
    completion.sort()       # 오름차순으로 정렬

    for i in range(len(completion)):        # 반복문 실행
        if participant[i] != completion[i]: # 만약 서로 같지 않다면
            answer = participant[i]         # answer에 participant[i] 저장하고 반복문 종료
            break
    else:                                   # 반복문 종료 후에도 break 동작 안할 경우
        answer = participant[-1]            # participant 마지막 원소 값을 answer에 저장

    return answer                           # 결과값 return