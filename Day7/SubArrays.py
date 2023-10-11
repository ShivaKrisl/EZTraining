def subarray(a, n) :
      outer = []
      for i in range(0,n):
             internal = []
             for j in range(i, n) : 
                   for k in range(i, j+1) :
                        internal.append(a[k])
                        print(a[k], end=" ")
                        print("\n", end=" ")
             outer.append(internal)
                        
      print(*outer)
a=[1, 2,3,4,5]
n=len(a)
print("all non - empty subarrays are:-")
subarray(a, n) 