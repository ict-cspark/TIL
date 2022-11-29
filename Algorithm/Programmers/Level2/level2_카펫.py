# Programmers - Level2 - 카펫

def solution(brown, yellow):
    result = (brown - 4) // 2               # 약수의 곱으로 yellow를 찾기 위해 result 구하기

    for i in range(1, result + 1):          # result를 1부터 result + 1까지 반복문 실행
        if i > yellow:                      # i가 yellow 보다 크다면 반복문 종료
            break
        if yellow % i == 0:                 # yellow가 i에 의해 나눠지면
            j = result - i                  # j에 result - i값 대입
            if (i * j) == yellow:           # i * j가 yellow이면
                break                       # 반복문 종료
    if i > j:                               # 테두리를 더하기 위해 각각 2씩 더함
        answer = [i + 2, j + 2]
    else:
        answer = [j + 2, i + 2]
    return answer                           # 결과 출력