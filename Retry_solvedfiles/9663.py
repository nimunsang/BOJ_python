# https://www.acmicpc.net/problem/9663

N = int(input())
board = [0]*N

def check(idx):
    for i in range(idx):
        if board[idx] == board[i] or (idx-i) == abs(board[idx]-board[i]):
            return False
    return True

answer = 0
def solve(idx):
    global answer
    if idx == N:
        answer += 1
        return
    
    for i in range(N):
        board[idx] = i
        if check(idx):
            solve(idx+1)
        board[idx] = 0
        
solve(0)
print(answer)