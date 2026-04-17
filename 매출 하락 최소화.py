import sys
sys.setrecursionlimit(10**7)

def solution(sales, links):
    n = len(sales)
    
    tree = [[] for _ in range(n)]
    for a, b in links:
        tree[a-1].append(b-1)  # 0-index
    
    dp = [[0, 0] for _ in range(n)]
    
    def dfs(u):
        dp[u][0] = 0
        dp[u][1] = sales[u]
        
        if not tree[u]:  # leaf
            return
        
        extra = float('inf')
        must_attend = False
        
        for v in tree[u]:
            dfs(v)
            
            # 공통 부분
            if dp[v][0] < dp[v][1]:
                dp[u][0] += dp[v][0]
                dp[u][1] += dp[v][0]
                extra = min(extra, dp[v][1] - dp[v][0])
            else:
                dp[u][0] += dp[v][1]
                dp[u][1] += dp[v][1]
                must_attend = True
        
        # u가 불참인데 아무도 참석 안한 경우 → 강제 1명 참석
        if not must_attend:
            dp[u][0] += extra
    
    dfs(0)  # root = 0번 (CEO)
    
    return min(dp[0][0], dp[0][1])
