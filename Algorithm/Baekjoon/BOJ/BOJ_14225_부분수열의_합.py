# Baekjoon Online Judge - 부분수열의 합

'''
수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.
예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다.
하지만, 4는 만들 수 없기 때문에 정답은 4이다.
'''


def func(k, S):                             # func 함수 실행 (시작값, 수열 합)
    global result                           # result global로 호출
    if k == N:                              # k와 N이 같을 경우
        result.add(S)                       # result에 S를 추가 후 종료
        return

    func(k + 1, S)                          # 수열 값을 더하지 않고 k + 1의 값으로 호출
    func(k + 1, S + num[k])                 # S에 수열 값을 더하고 k + 1을 호출

    return


N = int(input())                            # 수열의 크기 N 입력받기
num = list(map(int, input().split()))       # 수열 입력받아 num에 저장

result = set()                              # 결과값들을 저장하기 위한 result set 생성
func(0, 0)                                  # func 함수 호출
result = sorted(list(result))               # result를 리스트로 변경 후 정렬

for i in range(len(result)):                # result 길이만큼 반복문 실행
    if result[i] != i:                      # 만약 result[i]의 값과 인덱스 i가 일치하지 않을 경우
        print(i)                            # 인덱스 i를 출력하고 반복문 종료
        break
else:                                       # 반복문을 다 돌 때까지 if문을 만나지 못하였을 경우
    print(len(result))                      # result의 길이 출력