from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    
    # ---------------------------
    # 1. 원형 → 선형 확장
    # ---------------------------
    weak_extended = weak + [w + n for w in weak]
    
    answer = len(dist) + 1  # 최대값보다 크게 설정
    
    # ---------------------------
    # 2. 시작점 선택
    # ---------------------------
    for start in range(length):
        
        # -----------------------
        # 3. 친구 순열 탐색
        # -----------------------
        for friends in permutations(dist):
            
            count = 1  # 사용한 친구 수
            # 첫 친구가 커버 가능한 범위
            position = weak_extended[start] + friends[count - 1]
            
            # -------------------
            # 4. 취약점 순회
            # -------------------
            for index in range(start, start + length):
                
                # 현재 친구로 커버 불가능하면
                if weak_extended[index] > position:
                    
                    count += 1  # 친구 추가
                    
                    # 친구 부족 → 종료
                    if count > len(dist):
                        break
                    
                    # 새 친구 투입
                    position = weak_extended[index] + friends[count - 1]
            
            # 최소값 갱신
            answer = min(answer, count)
    
    # ---------------------------
    # 5. 결과 반환
    # ---------------------------
    if answer > len(dist):
        return -1
    
    return answer
