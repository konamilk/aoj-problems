N, W = map(int, input().split())

v = []
w = []

W_max = 12000

# dp = np.zeros((N+1, W_max), dtype=int)
dp = [[0 for i in range(W_max)] for j in range(N+1)]

for i in range(N):
    vi, wi = map(int, input().split())
    v.append(vi)
    w.append(wi)

for i in range(N+1):
    if i == 0:
        continue

    for j in range(W_max):
        if j < w[i-1]:
            # dp[i, j] = dp[i-1, j]
            dp[i][j] = dp[i-1][j]
        else:
            # dp[i, j] = max(dp[i-1, j], dp[i-1, j-w[i-1]] + v[i-1])
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])

print(dp[N][W])