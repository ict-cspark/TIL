# Programmers - Level2 - 구명보트

'''
사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
'''

def solution(people, limit):
    answer = 0                  # 결과값 출력을 위한 answer 변수 생성
    people.sort()               # people 리스트를 오름차순으로 정렬

    start = 0                   # start index를 0으로 지정
    end = len(people) - 1       # end index를 len(people) - 1 로 지정

    while start <= end:         # start의 index가 end와 같을 때가지 반복문 실행
        answer += 1             # answer에 1을 추가
        # 만약 people[start] + people[end]의 값이 limit 보다 작거나 같다면
        if people[start] + people[end] <= limit:
            start += 1          # start의 index 값에 1을 더함 (오른쪽으로 이동)
        end -= 1                # end의 index 값에 1을 뺌 (왼쪽으로 이동)

    return answer               # answer 값을 반환
