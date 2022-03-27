# Baekjoon Online Judge - 후보 추천하기

'''
후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 최종 후보가 누구인지 결정하는 프로그램을 작성하시오.
'''

N = int(input())                                # 사진틀 길이 N 입력받기
S = int(input())                                # 추천 횟수 S 입력 받기
pick = list(map(int, input().split()))          # 추천 명단 입력받아 pick 리스트에 저장

student = dict()                                # 학생 정보 저장할 student 딕셔너리 저장
photo = []                                      # 사진틀 photo 리스트 생성

for p in pick:                                  # pick에 저장된 후보 추천 수만큼 반복문 실행
    if len(photo) < N:                          # 사진틀이 다 차지 않았다면
        if student.get(p):                      # 만약 후보 추천한적이 있다면
            student[p] += 1                     # 추천 수만 증가
        else:                                   # 추천한 적이 없다면
            photo.append(p)                     # 사진틀에 후보 추가하고
            student[p] = 1                      # 학생 딕셔너리에 생성 후 추천수 1 대입

    else:                                       # 사진틀이 꽉차있다면
        if student.get(p):                      # 만약 후보 추천한 적이 있다면 추천수만 증가
            student[p] += 1
        else:                                   # 사진틀이 꽉차있고 후보추천 받은 적 없다면
            answer = 9999                       # 추천수 비교할 answer 값 생성 후 9999로 초기화
            idx = 0                             # 학생 정보 저장할 idx 변수 생성
            for i in photo:                     # 사진틀에서 하나씩 불러와
                if answer > student.get(i):     # 후보추천수가 answer 보다 작다면
                    answer = student.get(i)     # answer에 추천 수 저장하고
                    idx = i                     # idx에 학생정보 저장
            photo.remove(idx)                   # idx에 저장된 학생을 사진틀에서 제거하고
            student.pop(idx)                    # 해당 학생을 학생 딕셔너리에서 제거

            photo.append(p)                     # 사진틀에 후보 추가하고
            student[p] = 1                      # 딕셔너리에 추천수 1로 변경

photo.sort()                                    # 사진틀 오름차순으로 정렬 후
for result in photo:
    print(result, end=' ')                      # 순서대로 출력