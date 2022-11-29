# Programmers - Level2 - 위장

def solution(clothes):

    clothes_hash = {}               # 해시 함수 사용을 위해 빈 딕셔너리 생성
    for name, sort in clothes:      # clothes 반복문 실행하여 종류별로 분류하여 갯수 구하기
        clothes_hash[sort] = clothes_hash.get(sort, 0) + 1

    answer = 1                      # 해시 함수 반복문 실행하여 조합할 수 있는 경우의 수 구하기
    for sort in clothes_hash:       # 예) 안입는 경우의 수 포함하여 2벌, 1벌은 3*2 = 6
        answer *= (clothes_hash[sort] + 1)

    return answer - 1               # 모두 안입는 경우 1가지를 빼주기
