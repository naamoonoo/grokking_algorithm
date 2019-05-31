import random

def quicksort(arr):
	if len(arr) < 2:
		return arr
	# if len(arr) == 2:
	# 	return arr if arr[0] < arr[1] else arr[::-1]
	# pivot = arr.pop(0)
	# left = []
	# right = []
	# for n in arr:
	# 	left.append(n) if pivot > n else right.append(n)
	pivot = arr[0]
	left = [n for n in arr[1:] if n <= pivot]
	right = [n for n in arr[1:] if n > pivot]
	return quicksort(left) + [pivot] + quicksort(right)

arr = list(range(10))
random.shuffle(arr)
print(arr)
print(quicksort(arr))
