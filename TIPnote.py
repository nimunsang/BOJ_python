#  이차원 배열의 시계방향 회전의 경우, list(zip(*arr[::-1])) 을 사용하자. (ex) [2020KAKAOBLIND] : 자물쇠와 열쇠
arr = [[0, 0, 0], [2, 2, 2], [1, 1, 1]]
for a in arr:
    print(*a)

arr = list(zip(*arr[::-1]))
for a in arr:
    print(*a)

#  반 시계 방향:
arr = [[0, 0, 0], [2, 2, 2], [1, 1, 1]]
arr = list(zip(*arr))[::-1]


#  DFS를 PYTHON으로 구현할 경우, setrecursionlimit을 이용해주자. (ex) BOJ[9466] : 텀 프로젝트

#  함수에 list를 인자로 넣을 경우, 시간 초과가 발생할 수 있다. (ex) BOJ[9466] : 텀 프로젝트

#  git에 staging된 것들을 되돌리고 싶다면 -> git reset HEAD





