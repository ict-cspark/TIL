import sys
sys.stdin = open('input.txt', 'r')

# 테스트 케이스 입력 받기
T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    # str1의 첫글자만 str2에서 있는지 검색하고 해당 인덱스를 리스트에 저장
    str_idx = []
    str2_len = len(str2)
    for i in range(str2_len):
        if str2[i] == str1[0]:
            str_idx.append(i)

    # str2에서 str_idx에 저장된 위치만 반복하여 str1과 일치하는지 검색
    str1_len = len(str1)
    for j in str_idx:
        for k in range(str1_len):
            # str2와 str1이 계속 일치하면 result를 1로 유지
            # 단 j + k 가 str2 인덱스 범위안에 있을 경우에만 실행
            if 0 < j + k < str2_len and str2[j+k] == str1[k]:
                result = 1
            # 반복문 도중에 한번이라도 다르다면 result를 0으로 바꾼후 break
            else:
                result = 0
                break
        # 만약 반복문을 마치고도 result가 1이라면 다음반복문 실행하지 않고 break
        if result == 1:
            break

    # 결과 출력
    print(f'#{t} {result}')




