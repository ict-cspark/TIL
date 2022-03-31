import sys
sys.stdin = open("input.txt", "r")


def partition(start, end):                          # Lomuto-Partiton 알고리즘 함수
    pivot = end                                     # pivot에 end 값 저장
    i = start - 1                                   # i는 start - 1 값으로 저장
    for j in range(start, end):                     # start부터 end까지 반복문 실행
        if num[j] < num[pivot]:                     # num[j]의 값이 num[pivot] 값보다 작다면
            i += 1                                  # i를 오른쪽을 1칸 이동하고
            num[i], num[j] = num[j], num[i]         # i와 j를 swap

    i += 1                                          # 반복문을 종료했을 경우 i를 오른쪽으로 1칸 이동하고
    num[i], num[pivot] = num[pivot], num[i]         # i와 pivot을 swap

    return i                                        # pivot 위치를 i로 변경하고 해당 값 리턴


def quick(start, end):                              # 퀵정렬을 수행하는 quick 함수 실행
    if start < end:                                 # 만약 start가 end 보다 작다면
        pivot = partition(start, end)               # LP 알고리즘 파티션 함수 실행 후 pivot에 반환 값 저장
        quick(start, pivot - 1)                     # start, pivot - 1 값으로 quick 함수 호출
        quick(pivot + 1, end)                       # pivot + 1, end 값으로 quick 함수 호출

    return num


# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())                                # 리스트의 길이 N 입력받기
    num = list(map(int, input().split()))           # 숫자 입력받아 num 리스트에 저장

    result = quick(0, N - 1)                        # quick 함수 실행하고 리턴값 result에 저장
    print(f'#{test_case} {result[N//2]}')           # result[N//2] 값을 출력