d = {
    0:[[1,2],[2,3]],
    1:[[2,4],[3,5],[4,1]],
    2:[],
    3:[[2,7],[4,2]],
    4:[]
}

dp = [float('inf') for i in range(len(d))]
i=0
dp[i] = 0
keys = list(d.keys())
for i in keys:
    dp[i] = min(dp[i],)
