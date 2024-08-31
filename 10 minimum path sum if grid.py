def f(r,c):
    if r==0 and c==0:
        return num[0][0]
    if r<0 or c<0:
        return 10**10  #inf value bcz we dont need to consider it min(any,inf)=any
    if dp[r][c]!=0:
        return dp[r][c]
    up=num[r][c]+f(r-1,c)
    left=num[r][c]+f(r,c-1)
    dp[r][c]=min(up,left)
    return dp[r][c]
    

dp=[]
num=[[5,9,6],[11,5,2]]
for i in range(len(num)):
    chunk=[]
    for j in range(len(num[i])):
        chunk.append(0)    
    dp.append(chunk)
total=num[-1][-1]
f(len(num)-1,len(num[0])-1)
print(dp[-1][-1])
#tabulation
dp=[]
num=[[5,9,6],[11,5,2]]
for i in range(len(num)):
    chunk=[]
    for j in range(len(num[i])):
        chunk.append(0)    
    dp.append(chunk)

dp[0][0]=num[0][0]
for i in range(len(num)):
    for j in range(len(num[i])):
        if i==0 and j==0:
            dp[i][j]=num[i][j]
            continue
        up,left=10**4,10**4
        if i>0:
            up=dp[i-1][j]+num[i][j]
        if j>0:
            left=dp[i][j-1]+num[i][j]
        dp[i][j]=min(up,left)
print(dp[-1][-1])

##spce optimization
prev_r=[0]*len(num)
for i in range(len(num)):
    curr_r=[0]*len(num[i])
    for j in range(len(num[i])):
        if i==0 and j==0:
            curr_r[j]=num[i][j]
            continue
        up,left=10**4,10**4
        if i>0:
            up=prev_r[j]+num[i][j]
        if j>0:
            left=curr_r[j-1]+num[i][j]
        curr_r[j]=min(up,left)
    prev_r=curr_r
print(prev_r)

#if maximum req

prev_r=[0]*len(num)
for i in range(len(num)):
    curr_r=[0]*len(num[i])
    for j in range(len(num[i])):
        if i==0 and j==0:
            curr_r[j]=num[i][j]
            continue
        up,left=0,0
        if i>0:
            up=prev_r[j]+num[i][j]
        if j>0:
            left=curr_r[j-1]+num[i][j]
        curr_r[j]=max(up,left)
    prev_r=curr_r
print(prev_r)