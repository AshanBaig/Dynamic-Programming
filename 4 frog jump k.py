#memo
def f(n):
    if n<=0:
        return 0
    if dp[n] !=-1:
        return dp[n] 
    jump=max(num)
    for j in range(1,k+1):
        jump=min(jump,f(n-k)+abs(num[j]-num[j-k]))
    dp[n]=jump
    return dp[n]
    
num=[30,10,60,10,60,50]
k=3
dp=[-1]*len(num)
f(len(num)-1)
print(dp[-1])
#TC = (O(N)*K)  K times loop chle ga
#SC =O(N)+O(N)
#tabular 
dp=[-1]*len(num)
dp[0]=0
jump=max(num)
for i in range(1,len(num)):
    for j in range(1,k+1):
        if i-j>-1:
            jump=min(jump,dp[i-j]+abs(num[i]-num[i-j]))
    dp[i]=jump
print(dp[-1])
#TC = O(N)
#SC = 0(N)
#space optimization yes we can do but this time O(K)
#but no need for this code its not necessory


