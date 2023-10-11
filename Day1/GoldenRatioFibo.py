# Fibonacci using Golden Ratio
import math
def Fibonacci(n):
    return int((math.pow((1+math.sqrt(5))/2,n)/math.sqrt(5)) - (math.pow((1-math.sqrt(5))/2,n)/math.sqrt(5)))
print(Fibonacci(100))
for i in range(0,10):
    print(Fibonacci(i),end = " ")