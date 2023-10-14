def coinchange(l,tar):
    dp = [[float('inf') for j in range(tar+1)] for i in range(len(l)+1)]
    # print(dp)
    for i in range(tar+1):
        dp[1][i] = i//l[0]
    print(*dp)
    for i in range(len(l)+1):
        for j in range(tar+1):
            # elif l[i-1]==j:
            #     dp[i][j] = 1
            if i==0 or j==0:
                continue
            if l[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j] = min(1+dp[i][j-l[i-1]],dp[i-1][j])
    return dp[len(l)][tar]
l = list(map(int,input().split()))
tar = int(input())
print(coinchange(l,tar))