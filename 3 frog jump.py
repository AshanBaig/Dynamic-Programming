# memoization
def f(n):
    if n<=0:
        return 0
    if arr[n]!=-1:
        return arr[n]
    left=f(n-1)+abs(num[n]-num[n-1])
    if n>1:
        right=f(n-2)+abs(num[n]-num[n-2])
    else:
        right=max(num)
    arr[n]=min(left,right)
    return arr[n]
num=[30,10,60,10,60,50]
arr=[-1]*(len(num))
f(len(num)-1)
print(arr[-1])
#Tabular 
n=[30,10,60,10,60,50]
dp=[-1]*len(n)
dp[0]=0
energy=0
for i in range(1,len(n)):
    jump1=dp[i-1]+(abs(n[i-1]-n[i]))
    if i>1:
        jump2=dp[i-2]+(abs(n[i-2]-n[i]))
    else:
        jump2=max(n)
    dp[i]=min(jump1,jump2)
    energy=dp[i]
print(energy)
#TC = O(N)
#SC =O(N)
####space optimization
prev1=0
prev2=0
for i in range(1,len(n)):
    left=prev1+(abs(n[i]-n[i-1]))
    if i>1:
        right=prev2+(abs(n[i]-n[i-2]))
    else:
        right=max(n)
    energy=min(left,right)
    prev2=prev1
    prev1=energy
print(energy)