#Task 1

l=[]
n=int(input("enter a range"))
global sum1
sum1=0
for i in range(n):
    num=int(input("enter a number"))
    l.append(num)
print(l)

for i in range(1,n+1):
    sum1+=i
    


def missingNumber(l):
    sum2=0
    for i in  l:
        sum2+=i
    if sum1!=sum2:
        print(sum1-sum2)
             #print(sum2)
missingNumber(l)
    
