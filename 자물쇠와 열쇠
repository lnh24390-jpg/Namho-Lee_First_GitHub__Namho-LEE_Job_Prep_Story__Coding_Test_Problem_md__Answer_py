# key를 시계 방향으로 90도 회전시키는 함수
def rotate(key):
    n = len(key)
    
    # 새로운 2차원 배열 생성
    # 회전 공식:
    # new[i][j] = key[n - j - 1][i]
    # → 행과 열을 바꾸면서 뒤집는 구조
    return [[key[n - j - 1][i] for j in range(n)] for i in range(n)]


# 자물쇠가 열렸는지 확인하는 함수
def check(new_lock):
    n = len(new_lock) // 3  # 원래 lock 크기
    
    # 확장된 배열의 중앙 영역만 검사
    # (n ~ 2n-1 범위가 실제 lock 위치)
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            
            # 하나라도 1이 아니면 실패
            # → 0이면 홈이 안 채워진 상태
            # → 2이면 돌기끼리 충돌한 상태
            if new_lock[i][j] != 1:
                return False
    
    # 모든 칸이 정확히 1이면 성공
    return True


def solution(key, lock):
    n = len(lock)  # lock 크기
    m = len(key)   # key 크기
    
    # -------------------------------
    # 1. 확장 배열 생성 (3배 크기)
    # -------------------------------
    # key가 lock 밖에서도 움직일 수 있도록
    # 충분한 공간 확보
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    # -------------------------------
    # 2. 중앙에 lock 삽입
    # -------------------------------
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    
    # -------------------------------
    # 3. key를 4번 회전하며 탐색
    # -------------------------------
    for _ in range(4):
        key = rotate(key)  # 90도 회전
        
        # ---------------------------
        # 4. 모든 위치에 대해 이동
        # ---------------------------
        # (0 ~ 2n 범위에서 이동)
        for x in range(2 * n):
            for y in range(2 * n):
                
                # -------------------
                # 5. key를 lock 위에 덮기
                # -------------------
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                # -------------------
                # 6. lock이 열렸는지 검사
                # -------------------
                if check(new_lock):
                    return True
                
                # -------------------
                # 7. 원상복구 (백트래킹)
                # -------------------
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    # 모든 경우를 시도했지만 실패
    return False
