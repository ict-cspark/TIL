# Programmers - Level2 - 큰 수 만들기


def solution(number, k):
    num_list = list(number)                         # 입력받은 number를 리스트로 변환
    result = []                                     # 결과값 저장을 위한 result 리스트 생성

    start = 0                                       # 인덱스 값 저장을 위한 start 변수 생성
    while k > 0:                                    # k가 0보다 클 때만 반복문 실행
        max_num = -1                                # max_num 변수 생성하고 초기값 -1로 대입
        max_idx = 0                                 # max_idx 변수 생성하고 초기값 0으로 대입
        for i in range(start, start + k + 1):       # start에서 start + k + 1 범위 내에서
            if num_list[i] == '9':                  # 만약 num_list[i]가 '9'라면
                max_idx = i                         # max_idx에 i를 저장하고 종료
                break
            if max_num < int(num_list[i]):          # max_num보다 num_list[i]가 크다면
                max_num = int(num_list[i])          # max_num을 교체
                max_idx = i                         # max_idx를 i로 교체

        result.append(num_list[max_idx])            # result에 num_list[max_idx] 추가
        k -= (max_idx - start)                      # k를 max_idx - start 값 빼기
        start = max_idx + 1                         # start는 max_idx + 1 더하기

        if (len(num_list) - start) == k:            # 만약 num_list - start 의 값과 k가 같다면
            start += k                              # start에 k를 더하고 반복문 종료
            break

    if start < len(num_list):                       # 만약 start 보다 num_list의 크기가 크다면
        result = result + num_list[start:]          # result 에 num_list 추가
    answer = "".join(result)                        # answer에 result를 join하여 대입
    return answer
