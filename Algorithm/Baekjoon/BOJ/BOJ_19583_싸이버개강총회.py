# Baekjoon Online Judge - 싸이버개강총회

import sys
input = sys.stdin.readline

partyStart, partyEnd, StreamEnd = map(str, input().split())

student = set()
result = 0
while True:
    try:
        chatTime, studentName = map(str, input().split())

        if chatTime <= partyStart:
            student.add(studentName)

        elif partyEnd <= chatTime <= StreamEnd:
            if studentName in student:
                student.remove(studentName)
                result += 1

    except ValueError:
        break

print(result)
