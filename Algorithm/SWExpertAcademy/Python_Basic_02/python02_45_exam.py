# 파이썬 기초(2) 45차시 5. 객체지향 - 연습문제 2

# Q. 국적을 출력하는 printNationality 정적 메서드를 갖는 Korean 클래스를 정의하고
# 메서드를 호출하는 코드를 작성해봅시다.

class Korean:
    Nationality = "대한민국"

    @classmethod
    def printNationality(cls):
        return cls.Nationality

print(Korean.printNationality())
print(Korean.printNationality())