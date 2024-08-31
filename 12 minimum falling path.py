#when you have different start and end 
#memoization
def f(r,c):
        if r==0:
            r_dg,l_dg=10**4,10**4
            if c>0:
                l_dg=matrix[r][c-1]
            if c+1<len(matrix):
                r_dg=matrix[r][c+1]
            return min(matrix[r][c],l_dg,r_dg)
        l_dg,r_dg=10**4,10**4
        if r<0 or c<0:
            return 10**4
        if dp[r][c]!=0:
            return dp[r][c]
        l_dg=matrix[r][c]+f(r-1,c-1)
        if c+1<len(matrix):
            r_dg=matrix[r][c]+f(r-1,c+1)
        straight=matrix[r][c]+f(r-1,c)
        dp[r][c]=min(straight,r_dg,l_dg)
        return min(straight,r_dg,l_dg)
mini=10**4
matrix=[[2,1,3],[6,5,4],[7,8,9]]
dp=[]
for i in range(len(matrix)):
    chunk=[]
    for j in range(len(matrix[i])):
        chunk.append(0)    
    dp.append(chunk)
for start in range(len(matrix)-1,-1,-1):
    mini=min(mini,f(len(matrix)-1,start))

print(mini)
#TC O(mxn)
# SC O(mxn) for mat + O(N for recursion)
#tabulation
dp=[]
for i in range(len(matrix)):
    chunk=[]
    for j in range(len(matrix[i])):
        chunk.append(0)    
    dp.append(chunk)
for j in range(len(matrix[0])):
    dp[0][j]=matrix[0][j]
print(dp)
# for start in range(len(matrix[0])): #start from 1st row and every column one by one
for r in range(1,len(matrix)):
        for c in range(0,len(matrix[0])):
            #base case
            l_dg,r_dg=10**4,10**4
            if c>0:
                l_dg=matrix[r][c]+dp[r-1][c-1]
            if c+1<len(matrix):
                r_dg=matrix[r][c]+dp[r-1][c+1]
            straight=matrix[r][c]+dp[r-1][c]
            dp[r][c]=min(l_dg,r_dg,straight)

print(matrix)
print(min(dp[-1]))
#space optimisation
prev_r=matrix[0]
# for start in range(len(matrix[0])): #start from 1st row and every column one by one
for r in range(1,len(matrix)):
        curr_r=[]
        for c in range(0,len(matrix[0])):
            #base case
            l_dg,r_dg=10**4,10**4
            if c>0:
                l_dg=matrix[r][c]+prev_r[c-1]
            if c+1<len(matrix):
                r_dg=matrix[r][c]+prev_r[c+1]
            straight=matrix[r][c]+prev_r[c]
            curr_r.append(min(l_dg,r_dg,straight))
        prev_r=curr_r
print(matrix)
print(min(prev_r))
 