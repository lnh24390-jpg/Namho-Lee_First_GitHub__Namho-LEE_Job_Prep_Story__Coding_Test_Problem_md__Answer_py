def solution(board):
    # 행, 열 크기
    n = len(board)
    m = len(board[0])
    
    # 최대 정사각형 한 변 길이
    max_size = 0
    
    # DP를 기존 board에 그대로 적용 (메모리 절약)
    for i in range(n):
        for j in range(m):
            
            # 첫 행/열은 그대로 사용
            if i == 0 or j == 0:
                max_size = max(max_size, board[i][j])
                continue
            
            # 현재 값이 1일 때만 확장 가능
            if board[i][j] == 1:
                board[i][j] = min(
                    board[i-1][j],     # 위
                    board[i][j-1],     # 왼쪽
                    board[i-1][j-1]    # 좌상단
                ) + 1
                
                max_size = max(max_size, board[i][j])
    
    # 넓이 = 한 변 길이의 제곱
    return max_size ** 2
