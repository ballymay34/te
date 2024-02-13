# 16. Даны две последовательности, требуется найти длину
# их наибольшей общей подпоследовательности.

# ejudge: https://new.contest.yandex.ru/48706/problem?id=215/2023_04_11/LfJ9C3F9xp
def lcs_len(a, b):
    n = len(a)
    m = len(b)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n):
        for j in range(1, m):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n-1][m-1]
# n = int(input())
# a = [int(x) for x in input().split()]
# m = int(input())
# b = [int(x) for x in input().split()]
# print(lcs_len(a, b))