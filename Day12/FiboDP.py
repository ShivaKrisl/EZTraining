def fibonacci(n,dp):
    if n<=1:
        return dp[n]
    elif dp[n]==0:
        dp[n] = fibonacci(n-1,dp)+fibonacci(n-2,dp)
    return dp[n]
n = int(input())
dp = [0 for i in range(n+1)]
dp[1] = 1
print(dp)
print(fibonacci(n,dp))
print(dp)