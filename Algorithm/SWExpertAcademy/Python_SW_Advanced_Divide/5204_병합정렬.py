import sys
sys.stdin = open("input.txt", "r")


def merge(left, right):                                 # merge 함수 실행
    l = 0                                               # left의 현재 인덱스를 저장하기 위한 l 변수 생성
    r = 0                                               # right의 현재 인덱스를 저장하기 위한 r 변수 생성
    answer = []                                         # 병합 되는 리스트를 저장하기 위한 answer 리스트 생성

    while l < len(left) and r < len(right):             # l과 r이 각각 리스트의 인덱스 범위 일경우만 반복문 실행
        if left[l] < right[r]:                          # left와 right의 현재 값을 비교하여 left가 작다면
            answer.append(left[l])                      # answer에 left의 값을 추가하고
            l += 1                                      # 가리키는 위치 1 이동
        else:
            answer.append(right[r])                     # right가 작을 경우 answer에 right 추가하고
            r += 1                                      # 가리키는 위치 1 이동

    while l < len(left):                                # 만약 l의 위치가 left 끝까지 도달하지 않았다면
        answer.append(left[l])                          # answer에 끝까지 도달할 때까지 계속 추가
        l += 1

    while r < len(right):                               # 만약 r의 위치가 right 끝까지 도달하지 않았다면
        answer.append(right[r])                         # answer에 끝까지 도달할 때까지 계속 추가
        r += 1

    return answer                                       # answer리스트를 리턴


def mergeSort(arr):                                     # mergeSort 함수 실행
    global cnt                                          # cnt를 global로 호출
    if len(arr) <= 1:                                   # arr 리스트의 길이가 1 이하일 경우
        return arr                                      # arr를 리턴

    m = len(arr) // 2                                   # arr리스트의 중간인덱스 값 저장
    left = mergeSort(arr[:m])                           # arr[:m]의 리스트로 mergeSort 호출해서 left에 저장
    right = mergeSort(arr[m:])                          # arr[m:]의 리스트로 mergeSort 호출해서 right에 저장
    if left[-1] > right[-1]:                            # 만약 left의 끝 원소가 right의 끝 원소보다 크다면
        cnt += 1                                        # cnt에 1을 추가
    answer = merge(left, right)                         # merge를 호출하고 리턴 값 answer에 저장

    return answer                                       # answer를 리턴


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                    # 숫자 갯수 N 입력받기
    num = list(map(int, input().split()))               # 숫자 입력받아 num 리스트에 저장

    cnt = 0                                             # 경우의 수를 세기 위한 cnt 변수 생성
    result = mergeSort(num)                             # mergeSort 함수를 실행하고 리턴 값 result에 저장

    print(f'#{test_case} {result[N // 2]} {cnt}')       # result 리스트의 중간인덱스 값과 cnt 출력