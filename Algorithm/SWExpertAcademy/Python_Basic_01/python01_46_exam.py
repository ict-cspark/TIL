# 파이썬 기초(1) 46차시 9. 내장함수 - 연습문제 4

# Q. "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
# 같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
# 알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.

word = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
lst = list(word)
num = list(map(lambda x: 4 if x == 'A' else 3 if x == 'B' else 2 if x == 'C' else 1,lst))
print(sum(num))