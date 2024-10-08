#Recurrsion
def f(r,c):
    if r<0 or c<0:
        return 0
    # dp.append([r,c])
    if r==0 and c==0:
        return 1
    # if dp[r][c]!=[-1,-1]:
    #     return dp[r][c]
    up=f(r-1,c)
    left=f(r,c-1)
    return up+left  #find all possible ways means uper jane ke or left jane ke kitne raste hain
n=[3,3]
# dp=[]
# for i in range(n[0]):
#     chunk=[]
#     for j in range(n[1]):
#         chunk.append(-1)    
#     dp.append(chunk)
print(f(n[0]-1,n[1]-1))
# print(dp)
# TC O(2^(m*n))    for every box we have 2 choices okay and we have r*c boxes so 2^(m*n)
# SC O(path length)  only stack path length ke brabr hoga jo answer aya jese 6 in other word (m-1)+(n-1)
#memoization
def f(r,c):
    if r<0 or c<0:
        return 0
    if r==0 and c==0:
        return 1
    if dp[r][c]!=-1:
        return dp[r][c]
    up=f(r-1,c)
    left=f(r,c-1)
    dp[r][c]=up+left
    return up+left

n=[4,4]
dp=[]
for i in range(n[0]):
    chunk=[]
    for j in range(n[1]):
        chunk.append(-1)    
    dp.append(chunk)
f(n[0]-1,n[1]-1)
print(dp[-1][-1])
#TC  O(m*n)
#SC O((m-1)+(n-1))*O(m,n)
#Tablulation
dp=[]
for i in range(n[0]):
    chunk=[]
    for j in range(n[1]):
        chunk.append(0)    
    dp.append(chunk)
dp[0][0]=1
for i in range(n[0]):
    for j in range(n[1]):
        if i==0 and j==0:
            continue
        #why we didnt take down and right bcz we are chosing from previsous value and we are going backword
        up=0
        left=0
        if i>0:up=dp[i-1][j]
        if j>0:left=dp[i][j-1]
        dp[i][j]=up+left
print(dp[-1][-1])
#TC O(m*n)
#SC o(m*n)
###Space optimization
dp=[]
for i in range(n[0]):
    chunk=[]
    for j in range(n[1]):
        chunk.append(0)    
    dp.append(chunk)
# dp[0][0]=1
#for any number we just need up one and left one so we can have only 1 prev_row
n=[4,4]
prev_r=[0]*n[1]
for i in range(n[0]):
    curr_r=[0]*n[1]
    for j in range(n[1]):
        if i==0 and j==0:
            curr_r[0]=1
            continue
        #why we didnt take down and right bcz we are chosing from previsous value and we are going backword
        up=0
        left=0
        if i>0:up=prev_r[j]
        if j>0:left=curr_r[j-1]
        curr_r[j]=up+left
    prev_r=curr_r
print(prev_r)

obstacleGrid =[[0,0,0],[0,1,0],[0,0,0]]
for i in range(len(obstacleGrid)):
        curr_r=[0]*len(obstacleGrid[i])
        for j in range(len(obstacleGrid[i])):
            if i==0 and j==0:
                curr_r[0]=1
                continue
            if obstacleGrid[i][j]==1:
                curr_r[j]=0
                continue
            #why we didnt take down and right bcz we are chosing from previsous value and we are going backword
            up=0
            left=0
            if i>0:up=prev_r[j]
            if j>0:left=curr_r[j-1]
            curr_r[j]=up+left
        prev_r=curr_r
print(prev_r[-1])