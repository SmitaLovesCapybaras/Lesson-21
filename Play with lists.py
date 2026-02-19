L=[5, 7, 2, 6, 10, 4, 3, 1, 8, 9]
print("Original list :", L)
count=0
for i in L:
    count+=i
avg=count/len(L)
print("sum=", count)
print("average=", avg)
L.sort()
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])