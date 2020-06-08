#ナップザックDP
n,W=map(int,input().split())
v,w=[],[]
for i in range(n):
    v_,w_=map(int,input().split())
    v.append(v_)
    w.append(w_)
dp=[[0]*(W+1) for _ in range(n+1)]
for i in range(n):
    for j in range(W+1):
        if j>=w[i]:
            dp[i+1][j]=max(dp[i][j-w[i]]+v[i],dp[i][j])
        else:
            dp[i+1][j]=dp[i][j]
print(dp[n][W])