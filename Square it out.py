L=[1,2,3,4,5,6,7,8,9,10]
print("Original list :", L)
count=0
for i in L:
    count+=i
avg=count/len(L)
print("square root=", count**0.5)
print("average=", avg)
L.sort()
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])