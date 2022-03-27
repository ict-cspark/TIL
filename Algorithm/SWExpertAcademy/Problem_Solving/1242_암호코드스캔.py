import sys
sys.stdin = open("input.txt", "r")

# code 딕셔너리를 생성하게 된 이유
# 암호코드의 길이가 가변적이므로 코드 7자리 전체를 하나씩 비교하기 보다는 넓이 비를 이용하여 찾기 위해
# 뒤에서 부터 비교하고 암호코드의 맨 앞자리는 모두 0이므로 비교가 무의미해 2,3,4번째 넓이 비만 이용함
# 모든 암호가 0-1-0-1로 교차하여 나오기 때문에 각각 갯수를 구해 첫번 째를 제외한 2,3,4의 패턴을 찾아 code에서 값을 찾기
code = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}

# 테스트케이스 입력받기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())                    # 세로 크기와 가로 크기 N, M 입력 받기
    ARR = [input().rstrip() for _ in range(N)]          # 암호코드 배열 ARR 입력받고 런타임 에러를 방지하기 위해 rstrip 사용
    ARR = list(set(ARR))                                # 입력받은 ARR 배열에서 set을 이용하여 중복 제거
    ARR.remove('0' * M)                                 # 중복제거한 ARR 배열에서 0으로만 이루어진 요소 제거

    password = []                                       # 2진수로 된 암호코드를 저장하기 위한 password 리스트 생성
    for hexa in ARR:                                    # ARR 리스트 내 요소 갯수만큼 반복문 실행
        bina = ''                                       # 2진수 저장을 위한 bina 변수 생성
        for h in hexa:                                  # hexa 길이만큼 반복문 실행
            deci = int(h, base=16)                      # 16진수 h를 10진수로 변환
            bina += format(deci, 'b').zfill(4)          # 10진수를 2진수로 변환 후 4자리가 안될 시 zfill를 이용하여 왼쪽부터 0으로 채우고 bina에 추가
        password.append(bina)                           # bina를 password 리스트에 추가

    result = []                                         # 유효한 암호코드 저장을 위한 result 리스트 생성
    for pwd in password:                                # password 리스트에서 하나씩 꺼내와 반복문 실행
        start = (M * 4) - 1                             # 시작지점으로 끝에서 부터 시작하기 위해 초기값 설정 (2진수로 변환했기 때문에 곱하기 4)
        while start >= 55:                              # start가 55보다 r같거나 클때까지 반복문 실행
            numbers = ['-'] * 8                         # 암호코드 저장을 위한 8자리의 numbers 리스트 생성
            if pwd[start] == '1':                       # pwd[start]의 값이 '1'일 경우 아래 조건문 실행
                for i in range(7, -1, -1):              # 암호코드 8자리 만큼 반복문 실행
                    pt1 = 0                             # 첫번째 패턴값 저장을 위한 pt1 생성 후 0으로 초기화
                    while pwd[start] == '1':            # pwd[start]의 값이 1이 나올때까지 계속 반복
                        pt1 += 1                        # pt1에 1을 더하고
                        start -= 1                      # strat 1 감소 (왼쪽으로 이동)
                    pt2 = 0                             # 두번째 패턴 찾기
                    while pwd[start] == '0':            # pwd[start]의 값이 0이 나올때까지 계속 반복
                        pt2 += 1                        # pt2에 1을 더하고
                        start -= 1                      # strat 1 감소 (왼쪽으로 이동)
                    pt3 = 0                             # 세번째 패턴 찾기
                    while pwd[start] == '1':            # pwd[start]의 값이 1이 나올때까지 계속 반복
                        pt3 += 1                        # pt3에 1을 더하고
                        start -= 1                      # strat 1 감소 (왼쪽으로 이동)
                    while pwd[start] == '0':            # 네번째 패턴 찾지 않고 다음 암호코드로 이동하기 위해 반복문 실행
                        start -= 1                      # 1이 나올때까지 start 1 감소 (왼쪽으로 이동)
                                                        # 암호코드 선 굵기를 알기 위해 패턴의 최솟값 K에 저장
                    K = min(pt1, pt2, pt3)              # 모든 암호코드 패턴에 1이 있기 때문에 최솟값이 선 굵기를 의미
                    key = str(pt3//K) + str(pt2//K) + str(pt1//K)   # 각 패턴에서 선 굵기 K로 나눈 몫을 문자열로 저장 후 역으로 더해 key에 저장
                    numbers[i] = code[key]              # numbers[i] 인덱스에 code 딕셔너리에서 key값을 이용해 값을 구하여 저장

                value = 0                               # 암호코드 검증을 위해 value 변수 생성
                for v in range(0, 8, 2):                # 암호코드 길이만큼 2씩 건너뛰며 반복문 실행
                    value += numbers[v] * 3             # 홀수번째의 값은 3을 곱하여 저장
                    value += numbers[v + 1]             # 짝수번째와 검증코드는 그대로 저장

                if value % 10 == 0:                     # value를 10으로 나눈 나머지가 없을 경우
                    result.append(tuple(numbers))       # number리스트를 tuple 형태로 result에 추가 ( 중복값 제거를 위해)
            
            else:
                start -= 1                              # pwd[start]값이 0일 경우 -1을 하여 왼쪽으로 이동
                                                        # 암호코드의 합이 아닌 암호 자체를 비교하기 위해 tuple 형태로 비교
    result = list(set(result))                          # 8자리 암호의 합이 같아도 암호 자체(순서)가 다르면 다른 암호이기 때문에 값을 추가해줘야 해서
    answer = 0                                          # result를 set로 변환하여 8자리 순서까지 똑같은 중복된 암호 제거 후 list로 다시 변환 
    for ans in result:                                  # 중복값이 제거 된 result 리스트를 불러와 반복문 실행
        answer += sum(ans)                              # ans 튜플의 합을 answer에 저장
    print(f'#{test_case} {answer}')                     # 결과값 출력