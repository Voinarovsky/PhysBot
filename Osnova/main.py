N, M = map(int, input().split())
MATRIX = []
for _ in range(N):
    NUMS = list(map(int, input().split()))
    MATRIX.append(NUMS)
for i in range(M):
    for j in range(N):
        print(MATRIX[j][i], end=' ')
    print()
