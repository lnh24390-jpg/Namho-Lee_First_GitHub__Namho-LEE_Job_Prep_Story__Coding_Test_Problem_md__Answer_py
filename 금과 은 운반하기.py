def solution(a, b, g, s, w, t):
    # 이분 탐색 범위 설정
    left = 0
    right = 10**15  # 충분히 큰 값 (최악의 경우 대비)
    answer = right

    # 이분 탐색 시작
    while left <= right:
        mid = (left + right) // 2  # 현재 시간 후보

        gold = 0    # 현재 시간 동안 운반 가능한 금
        silver = 0  # 현재 시간 동안 운반 가능한 은
        total = 0   # 금 + 은 총 운반량 (핵심 포인트)

        # 모든 도시 순회
        for i in range(len(g)):
            # 왕복 기준 이동 횟수
            trips = mid // (2 * t[i])

            # 마지막에 편도로 한 번 더 갈 수 있는 경우
            if mid % (2 * t[i]) >= t[i]:
                trips += 1

            # 해당 도시 트럭이 운반 가능한 최대 광물
            max_transport = trips * w[i]

            # 금, 은 각각 최대 운반량 누적
            gold += min(g[i], max_transport)
            silver += min(s[i], max_transport)

            # 금 + 은 총량 (같이 실을 수 있으므로 중요)
            total += min(g[i] + s[i], max_transport)

        # 목표 조건 만족 여부 체크
        if gold >= a and silver >= b and total >= a + b:
            # 조건 만족 → 더 작은 시간 탐색
            answer = mid
            right = mid - 1
        else:
            # 조건 불만족 → 시간 늘려야 함
            left = mid + 1

    return answer
