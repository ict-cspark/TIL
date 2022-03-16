# Programmers - Level2 - 캐시

'''
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.
'''

def solution(cacheSize, cities):
    cache = []                              # 캐시를 저장하기 위한 빈 리스트 생성
    answer = 0                              # 결과값 저장을 위한 빈 변수 생성

    if cacheSize:                           # 캐시의 크기가 0이 아니라면 아래 조건문 실행
        for city in cities:
            city = city.lower()             # 대소문자 구별을 안하기 때문에 값을 소문자로 변경
            if city in cache:               # city가 캐시에 존재할 경우 아래 조건문 실행
                cache.pop((cache.index(city)))  # 캐시에서 city의 위치를 찾은 다음 pop 하여 제거
                cache.append(city)          # 캐시의 맨뒤에 city 값을 다시 추가
                answer += 1                 # 캐시에 city가 있었으므로 answer에 1을 추가

            else:                           # city가 캐시에 존재하지 않을 경우 아래 조건문 실행
                if cacheSize == len(cache): # 만약 캐시가 다 찼다면
                    cache.pop(0)            # 캐시에서 맨앞의 요소를 pop하여 제거
                cache.append(city)          # 캐시 맨뒤에 city를 추가
                answer += 5                 # 캐시에 city가 없었으므로 answer에 5를 추가

    else:                                   # 캐시의 크기가 0이라면 값의 저장이 불가능하기 때문에
        answer = len(cities) * 5            # cities의 리스트 길이의 5를 곱한 값을 answer에 저장
    return answer                           # 결과값을 리턴