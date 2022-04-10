# Programmers - Level2 - [3차] n진수 게임

'''
이진수로 진행하는 게임에 익숙해져 질려가던 사람들은 좀 더 난이도를 높이기 위해 이진법에서 십육진법까지 모든 진법으로 게임을 진행해보기로 했다.
숫자 게임이 익숙하지 않은 튜브는 게임에 져서 벌칙을 받는 굴욕을 피하기 위해, 자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다.
튜브의 프로그램을 구현하라.
'''

alph = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}   # 11진수 ~ 16진수에서 사용할 alph 딕셔너리 생성


def solution(n, t, m, p):                           # 진법 n, 구할 숫자 갯수 t, 참여 인원 m, 순서 p
    num = ['0'] * (t * m)                           # 10진수에서 n진법으로 변환된 숫자를 저장하기 위한 num 리스트 생성
    for i in range(1, len(num)):                    # 1부터 num 리스트 길이만큼 반복문 실행
        change = ''                                 # 변환할 숫자를 저장하기 위한 chanae 변수 생성
        ans = i                                     # 변환할 숫자 인덱스를 ans 에 저장
        while ans > 0:                              # ans가 0이 될때까지 반복문 실행
            temp = ans % n                          # temp에 ans를 n으로 나눈 나머지를 저장
            if 10 <= temp <= 15:                    # 만약 나머지가 10이상 15이하일 경우
                temp = alph[temp]                   # 나머지를 alph 딕셔너리를 활용하여 알파벳으로 저장
            ans = ans // n                          # ans에 ans를 n으로 나눈 몫을 저장
            change = str(temp) + change             # change에 문자열로 바꾼 temp를 뒤에서 부터 차례대로 저장
        num[i] = change                             # 반복문 종료 후 num[i]에 change를 저장

    answer = ''.join(num)                           # num리스트에 저장된 숫자들을 answer의 하나의 문자열로 저장
    result = ''                                     # 결과를 출력하기 위한 result 변수 생성
    for j in range(t):                              # 구할 숫자 갯수만큼 반복문 실행
        result += answer[(j * m) + (p - 1)]         # j에 참여인원을 곱한 후 순서 - 1의 인덱스에 숫자를 result에 더함

    return result                                   # 결과값 출력