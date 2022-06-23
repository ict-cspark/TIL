# Baekjoon Online Judge - 회전 초밥


N, d, k, c = map(int, input().split())          # N, d, k, c 입력 받기
sushi = [int(input()) for _ in range(N)]        # sushi 입력 받기

max_result = 0                                  # 결과값을 구하기 위한 max_result 변수 생성 후 0으로 초기화
for i in range(N):                              # max_result == k 일 경우 break
    if max_result == k:
        break

    answer = set()                              # answer 생성하여 set으로 설정
    end = k + i                                 # end 변수 생성하여 k + i 초기화
    for j in range(i, end):                     # i 부터 end - 1 까지 반복문 실행
        j = j % N                               # j 는 j % N으로 변환
        if sushi[j] == c:                       # sushi[j] 가 c라면 continue
            continue
        answer.add(sushi[j])                    # sushi[j]를 answer에 추가
    if len(answer) > max_result:                # 만약 answer의 길이가 max_result보다 크다면
        max_result = len(answer)                # max_result를 answer 길이로 대입

print(max_result + 1)                           # max_result + 1 값으로 결과값 출력
