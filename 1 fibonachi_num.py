# Recursive Solution top down from n to base
def f(n):
    if n<=1: return n
    if dp[n]!=-1: return dp[n]
    dp[n]=f(n-1)+f(n-2)
    return dp[n]
# num=int(input('Enter positive num: '))
num=6
dp=[-1]*(num+1)
print(f(num))
'''time complexcity =  O(N)  means if user enter 5 then we just need to find f4,f3,f2,f1,f0 only 5 times recurssive calls 
Total Space Complexity
When you combine both factors:

Memoization Array: O(N)
Recursive Call Stack: O(N)
total space = O(N)+O(N)'''

#Tabulation Format bottom-up  means from base case to n
n=7
dp=[-1]*(n+1)
dp[0]=0
dp[1]=1
for i in range(2,n+1):
   dp[i]=dp[i-2]+dp[i-1] 
print(dp[-1])
# TC=O(N)
#SC=O(N) no stack here

###################
#more better that doesnt take O(N) space
n2=7
prev2=0
prev1=1
ans=0
for i in range(2,n2+1):
    ans=prev1+prev2
    prev2=prev1
    prev1=ans
print(ans)

# TC=O(N)
#SC=O(1) no stack here
