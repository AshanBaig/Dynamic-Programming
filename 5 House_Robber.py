#memoization
def f(n):
    if n<=1:
        dp[n]=num[n]
        return num[n]
    if dp[n]!=-1:
        return dp[n]
    left=0
    right=0
    if n-2>-1:
        left=f(n-2)+(num[n])
    if n-3>-1:
        right=f(n-3)+(num[n])
    
    dp[n]=max(left,right)
    return dp[n]
    
   
num=[2,1,4,9,1,10,15]
dp=[-1]*len(num)
last=f(len(num)-1)
second_last=f(len(num)-2)
print(dp)
print(max(dp))
#TC O(N)+O(N)
#SC O(N)+O(N)
############################################################
#tabular
# num= [1,2,3,1]
dp2=[0]*len(num)
total=0
right=-1
dp2[0],dp2[1]=num[0],num[1]
for i in range(2,len(num)):
    left=num[i]+dp2[i-2]
    if i-3>-1:
        right=num[i]+dp2[i-3]
    dp2[i]=max(left,right)
print(max(dp2))
#TC =O(N)
#SC =O(N)

##################################################
#optimal memorization
#here we need four arguments i think
# total=0
# prev2=0
# prev3=0
# prev4=0
# for i in range(len(num)-2):
#     prev2=num[i]
#     prev3=num[i+1]
#     prev4=num[i+2]
#     total+=max(prev2+prev4,prev3)
# # print(total)

        
#####################################################
# one more way pick not pick
dp=[0]*len(num)
def f(n):
    if n==0:
        return num[0]
    if n<0:
        return 0
    if dp[n]!=0:
        return dp[n]
    pick=num[n]+f(n-2)
    not_pick=0+f(n-1)
    dp[n]=max(pick,not_pick)
    return dp[n]
print(f(len(num)-1))
#TC O(N)
#SC O(N)+O(N)
#tabular
dp=[0]*len(num)
dp[0]=num[0]
for i in range(1,len(num)):
    take=num[i]
    if i>1:
        take+=dp[i-2]
    nottake=dp[i-1]
    dp[i]=max(take,nottake)
print(dp)
#TC O(N)
#SC O(N)
############
#space optimization
dp=[0]*len(num)
prev1=num[0]
prev2=0
for i in range(1,len(num)):
    take=num[i]
    if i>1:
        take+=prev2
    nontake=prev1
    curi=max(take,nontake)
    prev2=prev1
    prev1=curi
print(prev1)
#TC O(N)
#SC O(1)
        