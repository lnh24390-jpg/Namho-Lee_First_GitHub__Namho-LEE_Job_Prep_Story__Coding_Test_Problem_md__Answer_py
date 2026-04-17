import sys
sys.setrecursionlimit(10**6)

def solution(k, num, links):
    n = len(num)

    # 루트 찾기
    is_child = [False] * n
    for l, r in links:
        if l != -1:
            is_child[l] = True
        if r != -1:
            is_child[r] = True

    root = is_child.index(False)

    def check(limit):
        groups = 1  # 최소 1개 그룹

        def dfs(node):
            nonlocal groups

            if node == -1:
                return 0

            l, r = links[node]

            left = dfs(l)
            right = dfs(r)

            val = num[node]

            # 세 개 합 가능
            if left + right + val <= limit:
                return left + right + val

            # 하나만 선택 가능
            if min(left, right) + val <= limit:
                groups += 1
                return min(left, right) + val

            # 둘 다 못 붙임
            groups += 2
            return val

        dfs(root)
        return groups <= k

    # 이분 탐색
    left = max(num)
    right = sum(num)

    answer = right

    while left <= right:
        mid = (left + right) // 2

        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
