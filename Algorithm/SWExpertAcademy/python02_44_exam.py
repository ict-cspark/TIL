# 파이썬 기초(2) 44차시 5. 객체지향 - 연습문제 1

# Q. 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

class Student:
    def __init__(self,kor,eng,mat):
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat

    @property
    def kor(self):
        return self.__kor

    @property
    def eng(self):
        return self.__eng

    @property
    def met(self):
        return self.__mat


    def total(self):
        return self.__kor + self.__eng + self.__mat

kor,eng,mat = map(int,input().split(','))
score = Student(kor,eng,mat)
total = score.total()
print('국어, 영어, 수학의 총점: {0}'.format(total))