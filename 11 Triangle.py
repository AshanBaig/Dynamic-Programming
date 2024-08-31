'''Rules for Triangle its
    -we have to end at nth row but at any column so we cant go from exit to start because we have multiple exits
    -so we will start from 0,0 till last row 
    - base case is very simple just last row 
    -make sure your pointer wont go out of the boundary we can go down or diagonal  
    -if your are iterate reversely so prev_r must be reverse  after iner loop   
'''
#recursion+ memo

def f(r,c):
    if r==len(n)-1:
        return n[r][c]
    if dp[r][c]!=0:
        return dp[r][c]
    down=n[r][c]+f(r+1,c)
    diagonal=n[r][c]+f(r+1,c+1)
    dp[r][c]=min(down,diagonal)
    return dp[r][c]

n=[[1],[100,2],[1,200,300]]
dp=[]
dp=[[0]*len(n) for _ in n[-1]]
print(f(0,0))
print(dp)
#TC O(NxN) almost
#SC O(N)RSS +dp ki  *N=length of rows

n=[[1],[100,2],[104,200,100]]
dp=[]
dp=[[0]*len(n) for _ in n[-1]]
#what ever u write for recursion its opposite for tabulation
#base case are as many as no. of columns means element is last row
for j in range(len(n[-1])):
    dp[-1][j]=n[-1][j]
print(dp)
for r in range(len(n)-2,-1,-1): #not taking last row
    for c in range(len(n[r])-1,-1,-1): #we have to take all columns of 2nd last row
        down=n[r][c]+dp[r+1][c]
        diagonal=n[r][c]+dp[r+1][c+1]
        dp[r][c]=min(down,diagonal)
print(dp[0][0])        
# TC O(N*N)
# SC O(N*N)
##Space optimization from the tabulation we observe that we just mneed only prev_row


# n=[[1],[1,1],[8,4,1],[5,3,4,100]]
#what ever u write for recursion its opposite for tabulation
#base case are as many as no. of columns means element is last row
print('**************')
n=[[1],[-2,-5],[3,6,9],[-1,2,4,-3]]
prev_r=n[-1]
for r in range(len(n)-2,-1,-1): #not taking last row
    curr_r=[]
    for c in range(len(n[r])-1,-1,-1): #we have to take all columns of 2nd last row
        down=n[r][c]+prev_r[c]
        diagonal=n[r][c]+prev_r[c+1]
        curr_r.append(min(down,diagonal))
    prev_r=curr_r[::-1]  #kab loop ulta chla rhy tw prev_r ko ulta kro
print(prev_r[0])    
# TC O(NxN)
# SC O(N)