# Programmers - Level3 - 베스트앨범


def solution(genres, plays):
    answer = []

    music = {}                          # 장르별 판매량 정보 딕셔너리 생성
    music_total = {}                    # 장르별 총 재생 수 딕셔너리 생성

    for idx, (g, p) in enumerate(zip(genres, plays)):   # genres와 plays를 zip으로 결합 후 인덱스와 정보 반복문 출력
        if g not in music:              # 장르가 music 딕셔너리에 없을 경우
            music[g] = [(idx, p)]       # 인덱스와 재생횟수 담긴 튜플 생성
        else:
            music[g].append((idx, p))   # 있을 경우 music[g]에 추가

        if g not in music_total:        # 재생횟수도 같은 방식으로 실행
            music_total[g] = p
        else:
            music_total[g] += p

    music_total = sorted(music_total, key=lambda x: music_total[x], reverse=True)   # music_total을 총 재생횟수 내림차순으로 정렬

    for g in music_total:               # 내림차순으로 장르 반복문 실행하여
        music_temp = sorted(music[g], key=lambda x: x[1], reverse=True)             # 해당 장르 키값의 벨류를 불러와 재생횟수 기준으로 내림차순 정렬
        for idx, p in music_temp[:2]:   # 최대 2개까지 출력하여 idx값 answer에 추가
            answer.append(idx)

    return answer
