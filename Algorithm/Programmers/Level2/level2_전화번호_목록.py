# Programmers - Level2 - 전화번호 목록

'''
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
'''


def solution(phone_book):
    answer = True               # answer의 초깃값으로 True 저장
    phone_book.sort()           # phone_book 리스트 오름차순으로 정렬

    for i in range(len(phone_book) - 1):    # phone_book - 1 까지 반복문 실행
        if phone_book[i].startswith(phone_book[i + 1]): # phone_book[i] 와 다음 원소의 접두어가 같을 경우
            answer = False                  # answer에 False 대입
            return answer                   # answer를 return
    return answer                           # 반복문 끝까지 돌았을 경우 answer return
