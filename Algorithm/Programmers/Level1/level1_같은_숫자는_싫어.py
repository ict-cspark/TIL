# Programmers - Level1 - 같은 숫자는 싫어

'''
배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
'''


def solution(arr):
    answer = [arr[0]]                   # answer 리스트 생성 후 초기값으로 arr[0] 대입
    flag = arr[0]                       # flag 변수 생성 후 초기값으로 arr[0]으로 설정
    for i in range(1, len(arr)):        # 1부터 arr 길이만큼 반복문 실행
        res = arr[i]                    # res에 arr[i] 저장
        if flag != res:                 # flag와 res가 같지 않다면
            answer.append(res)          # answer 리스트에 추가 후
            flag = res                  # flag에 res값으로 수정
    return answer                       # answer 리턴
