# Programmers - Level2 - 오픈채팅방

'''
채팅방에 들어오고 나가거나,
닉네임을 변경한 기록이 담긴 문자열 배열 record가 매개변수로 주어질 때,
모든 기록이 처리된 후, 최
종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return 하도록 solution 함수를 완성하라.
'''


def solution(record):

    newRecord = []                          # 하나의 문자열로 들어온 입력을 단어별로 저장할 리스트 생성
    idStatus = dict()                       # id의 상태를 저장하기 위한 딕셔너리 생성
    for r in record:                        # record 길이만큼 반복문 실행
        nr = list(map(str, r.split()))      # 공백을 기준으로 분리하여 nr 리스트 생성
        newRecord.append(nr)                # nr리스트 newRecord에 추가
        if nr[0] != 'Leave':                # 만약 nr[0]의 상태가 Leave가 아니라면
            idStatus[nr[1]] = nr[2]         # idStatus에 key는 id, value는 닉네임 형태로 값 갱신 

    answer = []                             # 결과 출력할 리스트 생성
    message = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'} # 상태를 메시지로 변환할 딕셔너리 생성
    for ans in newRecord:                   # newRecord 길이만큼 반복문 실행
        if ans[0] != 'Change':              # ans[0]의 상태가 'Change' 가 아니라면
            result = idStatus[ans[1]] + message[ans[0]] # 닉네임과 상태 메시지를 결합하여 result에 저장
            answer.append(result)           # answer에 result 추가

    return answer                           # answer 반환