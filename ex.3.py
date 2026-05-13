import  time
import matplotlib.pyplot as plt
def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
x=[34,46,43,27,57,41,45,21,70]
print("before sorting:",x)
bubblesort(x)
print("after sorting:",x)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("bubblesort-time complexity is 0(n^2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()