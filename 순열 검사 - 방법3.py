def solution(arr):
    n = len(arr)
    
    # 합 공식: n(n+1)/2
    return sum(arr) == n * (n + 1) // 2 and len(set(arr)) == n
