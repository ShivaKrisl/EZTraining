def find(wt,pr,bag):
    dp = [[0 for j in range(bag+1)] for i in range(len(wt)+1)]
    for i in range(len(wt)+1):
        for j in range(bag+1):
            if j==0 or i==0:
                dp[i][j]=0
            elif wt[i-1]<=j:
                dp[i][j] = max(pr[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    # print(*dp)
    return dp[len(wt)][bag]
wt = list(map(int,input().split()))
pr = list(map(int,input().split()))
bag = int(input())
print(find(wt,pr,bag))