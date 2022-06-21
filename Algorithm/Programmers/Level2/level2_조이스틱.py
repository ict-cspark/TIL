# Programmers - Level2 - 조이스틱

def solution(name):
    answer = 0                  # 결과값을 구하기 위한 초기값 0 설정
    min_move = len(name) - 1    # 좌우 이동거리 기본값으로 단어 길이의 - 1 로 설정

    for idx, char in enumerate(name):   # name 크기 만큼 반복문 실행하여 인덱스와 글자 하나씩 출력

        # 단어를 위로 이동하는 것과 아래로 이동하는 것 중 최솟값을 answer에 저장
        answer += min(ord(char) - ord('A'), (ord('Z') + 1) - ord(char))

        next_value = idx + 1            # 연속된 A를 찾기 위해 idx + 1을 시작값으로 설정
        # next_value 값이 len(name)보다 작고 해당 인덱스 값이 'A'일 경우
        while next_value < len(name) and name[next_value] == 'A':
            next_value += 1             # 인덱스 값에 1을 더함

        # idx와 연속된 'A'의 인덱스가 저장되어 있는 next_value를 활용하여 왼쪽, 오른쪽 각각 이동했을
        # 값을 구한 뒤 min_move와 왼쪽으로 이동, 오른쪽으로 이동 된 값중 최솟값을 min_move에 저장
        min_move = min(min_move, (2 * idx + len(name) - next_value), idx + 2 * (len(name) - next_value))

    answer += min_move                  # answer에 min_move값 저장
    return answer                       # answer를 리턴
