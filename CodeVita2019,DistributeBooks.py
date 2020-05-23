mod=1000000007
def calculate(dp,n):
    for i in range(3,n+1):
        dp[i]=((i-1)*(dp[i-1]+dp[i-2]))%mod



n=int(input())
dp=[None]*(n+1)
dp[0]=1
dp[1]=0
dp[2]=1
calculate(dp,n)
print(dp[n])
