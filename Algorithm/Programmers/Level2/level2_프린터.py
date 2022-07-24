# Programmers - Level2 - 프린터

'''
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.
'''


def solution(priorities, location):
    result = []                                     # index 저장을 위한 result 리스트 생성
    for idx, order in enumerate(priorities):        
        result.append((order, idx))                 # result 리스트에 order와 idx 같이 저장

    answer = []                                     # answer 리스트 생성
    while result:                                   # result 리스트가 있을 때까지 반복문 실행
        res = result[0]                             # res의 초기값으로 result[0] 설정
        res_max = max(result)                       # res_max의 초기값으로 max(result) 설정
        if res[0] != res_max[0]:                    # 만약 res[0]과 res_max[0]이 같지 않다면
            temp = result.pop(0)                    # 첫번째 원소를 꺼내서
            result.append(temp)                     # result 마지막에 다시 추가
        else:                                       # 같을 경우
            temp = result.pop(0)                    # 첫번째 원소를 꺼내서
            answer.append(temp)                     # answer리스트에 추가


    for loc in range(len(answer)):                  # 답을 찾기 위한 반복문
        if answer[loc][1] == location:              # answer 원소의 idx값이 location과 같을 경우
            break                                   # 반복문 종료 후
    return loc + 1                                  # loc + 1값 리턴
