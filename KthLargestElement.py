#Task 6 Find Kth largest element
l=[]
n=int(input("enter a range"))
for i in range(n):
    num=int(input("enter a number"))
    l.append(num)
k=int(input("enter a element"))
def large(l2,k2):
    l2=list(set(l2))
    l2.sort(reverse=True)
    if k2<=len(l2):
        print(l2[k2-1])
    else:
        print("Invalid Input")
large(l,k)
