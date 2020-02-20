import sys 
arr1 = [64, 25, 12, 22, 11]
arr2 = [64, 34, 25, 12, 22, 11]
arr3 = [-64, 34, 25]
arr4 = []
  

def selectionSort(arr):
    n = len(arr)
    for i in range(n): 
        min_idx = i 
        for j in range(i+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j      
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
  
# Driver code to test above
selectionSort(arr1)
selectionSort(arr2)
selectionSort(arr3)
selectionSort(arr4)

print ("Sorted array1: ") 
print(arr1)
print ("Sorted array2: ") 
print(arr2)
print ("Sorted array3: ") 
print(arr3)
print ("Sorted array4: ") 
print(arr4)
