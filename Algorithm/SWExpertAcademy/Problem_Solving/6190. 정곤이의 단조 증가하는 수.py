# 6190. 정곤이의 단조 증가하는 수

'''
정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했다.

그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.

어떤 k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수이다.

예를 들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.

양의 정수 N 개 A1, …, AN이 주어진다.

 1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.
'''
import sys
sys.stdin = open("input.txt", "r")


def multi(arr):                         # 두수의 곱을 리스트로 반환하는 함수
    result = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            result.append(str(arr[i] * arr[j]))     # 두 수의 곱을 문자로 변환 후 출력
    return result


def numcheck(lst):              # 리스트 내 원소가 단조증가수인지 확인 후 최댓값을 반환
    result = []
    for num in lst:             # 리스트 내 원소 수만큼 반복
        for i in range(len(num) - 1):   
            if num[i] > num[i + 1]:     # 원소의 앞 자리가 뒷자리보다 클 경우 result에 -1을 추가 후 반복문 종료
                result.append(-1)
                break
        else:                   # 반복문을 모두 돌았을 경우 단조증가수임으로 정수로 변환후 result에 추가
            result.append(int(num))
    if result == []:            # result가 비어있을 경우 -1을 리턴
        return -1
    return max(result)          # 저장된 리스트 중에 최댓값을 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))

    numset = multi(num)             # 두 수의 곱이 담긴 리스트를 반환하는 함수
    result = numcheck(numset)       # 리스트의 원소 중에 단조 증가수를 찾아 최대값을 출력하는 함수
    # 결과값 출력
    print(f'#{test_case} {result}')