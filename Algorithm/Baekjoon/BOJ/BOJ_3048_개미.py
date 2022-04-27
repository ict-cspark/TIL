# Baekjoon Online Judge - 개미

'''
첫 번째 그룹이 ABC로 움직이고, 두 번째 그룹의 개미가 DEF순으로 움직인다고 하자.
그럼, 좁은 길에서 만났을 때, 개미의 순서는 CBADEF가 된다.
1초가 지났을 때는 자신의 앞에 반대방향으로 움직이는 개미가 있는 개미는 A와 D다.
따라서, 개미의 순서는 CBDAEF가 된다. 2초가 되었을 때, 자신의 앞에 반대 방향으로 움직이는 개미는 B,D,A,E가 있다.
따라서, 개미의 순서는 CDBEAF가 된다.
T초가 지난 후에 개미의 순서를 구하는 프로그램을 작성하시오.
'''


N, M = map(int, input().split())                # 개미의 수 N, M 입력받기
first = list(input())                           # 첫번째 그룹 first 리스트에 입력받기
second = list(input())                          # 두번째 그룹 second 리스트에 입력받기
T = int(input())                                # 시간 초 T에 입력받기

firstNew = first[::-1]                          # first 리스트 reverse 하여 firstNew에 저장

ants = firstNew + second                        # fristNew와 second 리스트를 더해 ants에 저장

for _ in range(T):                              # 시간 T만큼 반복문 실행
    for i in range(len(ants) - 1):              # ants의 길이 - 1 만큼 반복문 실행
        # anst[i]가 first에 있고 ants[i + 1]이 second에 있을 경우
        if ants[i] in first and ants[i + 1] in second:
            ants[i], ants[i + 1] = ants[i + 1], ants[i]     # 서로 switch

            if ants[i + 1] == first[0]:         # 만약 바꾼 개미가 첫번째 주자일 경우 더이상 이동 금지하기 위해 반복문 종료
                break

print(''.join(ants))                            # 결과 출력
