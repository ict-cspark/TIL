# Programmers - Level2 - 행렬의 곱셈

'''
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.
'''

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]
            temp.append(sum)
        answer.append(temp)

    return answer