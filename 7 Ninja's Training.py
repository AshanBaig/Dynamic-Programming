def f(n,last):
    if n==0:
        base=num[0].copy()
        base.pop(last)
        maxi=max(base)
        dp[n][last]=maxi
        return maxi         
    if dp[n][last]!=-1:
        return dp[n][last]
    maxi=0
    for i in range(3):
        if i==last:
            continue
        points=num[n][i]+f(n-1,i)
        maxi=max(maxi,points)
        dp[n][last]=maxi
    return maxi                    
    
    
num=[[2,1,3],[3,4,6],[10,1,6],[8,3,7]]
dp=[[-1,-1,-1,-1]  for _ in range(len(num))]    
print(dp)  
f(len(num)-1,3)
print(dp)
# TC O(N*4)*3   4 is bcz we have 4 cases of each n and 4 is we are iterate 3
#SC O(N)O(N*W)
#tabulation
dp=[[-1,-1,-1,-1]  for _ in range(len(num))]    
dp[0][0]=max(num[0][1],num[0][2])
dp[0][1]=max(num[0][0],num[0][2])
dp[0][2]=max(num[0][1],num[0][0])
# print(num[0])
dp[0][3]=max(num[0])
for i in range(1,len(num)):
    for j in range(4):
        maxi=0
        for task in range(3):
            if task!=j:
                points=num[i][task]+dp[i-1][task]
                maxi=max(points,maxi)
        dp[i][j]=maxi

print(dp[-1][3])