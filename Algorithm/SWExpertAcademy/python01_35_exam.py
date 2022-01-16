# 파이썬 기초(1) 35차시 8. 함수의 기초 - 연습문제 2

# Q. 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

usera = input()
userb = input()
gamea = input()
gameb = input()

def trans(game):
    if game == '가위':
        game = 1
    elif game == '바위':
        game = 2
    else:
        game = 3
    return game

def game(one,two):
    if one - two == -1 or one - two == 2:
        return two
    else:
        return one

def win(winner):
    if winner == 1:
        print("가위가 이겼습니다!")
    elif winner == 2:
        print("바위가 이겼습니다!")
    else:
        print("보가 이겼습니다!")

transa = trans(gamea)
transb = trans(gameb)
result = game(transa,transb)
winner = win(result)