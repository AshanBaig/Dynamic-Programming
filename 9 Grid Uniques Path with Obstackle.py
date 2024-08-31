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