# Programmers - Level2 - 튜플


def solution(s):
                                            # s를 슬라이싱 하여 {{와 }}를 제거 후 }
    s = s[2:-2].split('},{')                # },{를 기준으로 split하여 리스트에 저장
    number = []                             # 숫자만 저장하기 위해 nubmer리스트 생성
    for i in s:                             # s 길이만큼 반복문 실행
        number.append(i.split(','))         # i에서 ,를 기준으로 split하여 생긴 리스트를 number에 추가
    number.sort(key=len)                    # number를 len을 기준으로 오름차순 정렬

    answer = []                             # 결과값 저장하기 위한 answer리스트 새성
    for num in number:                      # number 길이만큼 반복문 실행
        for n in num:                       # num 길이만큼 반복문 실행
            if int(n) not in answer:        # answer에 int(n)이 없을 경우 
                answer.append(int(n))       # int(n)을 추가하고
                break                       # 반복문 종료

    return answer                           # 결과값 출력