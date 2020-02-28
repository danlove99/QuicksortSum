arr = [2,5,76,3,4, 15,6,32,1,5,8]
target = 16

def quicksort(arr):  
  length = len(arr) 
  if length <= 1:
    return arr
  else:
    pivot = arr.pop()
  greater=[]
  lesser=[]
  for i in arr:
    if i > pivot:
      greater.append(i)
    else:
      lesser.append(i)
  return quicksort(lesser) + [pivot] + quicksort(greater)


def findSum(arr, target):
  if len(arr) <= 1:
    return False
  low = 0
  high = len(arr) - 1
  print(arr[low], arr[high])
  for i in range(len(arr)):
    if arr[low] == arr[high]:
      pass
    elif arr[low] + arr[high] == target:
      return arr[low], arr[high]
    elif arr[low] + arr[high] < target:
      low +=1
    else:
      high -=1
    print(arr[low], arr[high])
  return False

print(findSum(quicksort(arr), target)) 
