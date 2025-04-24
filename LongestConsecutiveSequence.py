#Task 4 Lognest consecutive sequence

l=[]
n=int(input("enter a range"))
for i in range(n):
    num=int(input("enter a number"))
    l.append(num)

def longconse(L):
   L=list(set(L))
   L.sort()
   #print(L)
   long=1
   immediate=1
   for i in range(1,len(L)):
       if L[i]==L[i-1]+1:
          immediate+=1
          long=max(long,immediate)
       else:
           immediate=1
   print(long)
'''while l3[t]>0:
    rem=t%10
    print(rem)
    count+=1
    i/=10'''
longconse(l)
