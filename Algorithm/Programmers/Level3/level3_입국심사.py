# Programmers - Level3 - 입국심사

def solution(n, times):
    times.sort()                        # times 리스트 오름차순으로 정렬
    start = 0                           # 이분탐색을 위해 start와 end 생성
    end = times[-1] * n                 # end는 times 리스트의 가장 큰값에 n을 곱한 값으로 초기화
    while start <= end:                 # start가 end보다 커지기 전까지 반복문 실행
        mid = (start + end) // 2        # 중간값 mid를 (start + end) // 2의 값으로 결정
        traveler = 0                    # 입국 심사 인원을 저장할 traveler 변수 생성
        for time in times:              # times 리스트의 반복문을 실행하여
            traveler += mid // time     # traveler에 mid // time 의 값을 더함
        if n <= traveler:               # n보다 tarveler가 같거나 크다면
            end = mid - 1               # end를 mid - 1 로 변경
        else:                           # n보다 작다면
            start = mid + 1             # start를 mid + 1로 변경

    return start                        # start를 반환
