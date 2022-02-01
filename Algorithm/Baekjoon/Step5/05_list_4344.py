# Baekjoon Algorithm 5단계 List - 평균은 넘겠지

'''
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
'''

C = int(input())

for i in range(C):
    score = []
    score = list(map(int,input().split(' ')))
    avg = sum(score[1:])/score[0]
    
    num = 0
    for j in score[1:]:
        if j > avg:
            num += 1
    
    result = float(num/score[0]*100)
    print(f'{result:.3f}%')