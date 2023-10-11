def quick_sort(arr):
    if len(arr) <= 1:
        return arr
        
    pivot = arr[0]
    left = [arr[i] for i in range(1,len(arr)) if arr[i] <= pivot]
    right = [arr[i] for i in range(1,len(arr)) if arr[i] > pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
arr = [1,2,1,3,2,1,4,5,6,1,2,6]
print(arr)
result = quick_sort(arr)
print(result)