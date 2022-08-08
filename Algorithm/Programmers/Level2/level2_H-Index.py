# Programmers - Level2 - H-index

def solution(citations):
    answer = 0                  # answer 변수 생성하고 초기값 0으로 설정
    num = len(citations)        # citations 리스트 길이 num에 저장
    citations.sort()            # 오름차순으로 정렬
    for i in range(num):        # num 크기만큼 반복문 실행하면서
        if citations[i] >= num - i: # 만약 citations[i]의 값이 num - i 의 값보다 같거나 크다면
            answer = num - i    # answer에 num - i 저장하고
            break               # 반복문 종료
    return answer               # answer 리턴
