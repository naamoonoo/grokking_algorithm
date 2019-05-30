import random

def	find_smallest(arr):
	sm = arr[0]
	sm_i = 0
	for i in range(1, len(arr)):
		if sm > arr[i]:
			sm = arr[i]
			sm_i = i
	return sm_i

def selection_sort(arr):
	res = []
	for _ in range(len(arr)):
		res.append(arr.pop(find_smallest(arr)))
	return res

# ??
# def bubble_sort(arr):
# 	for i in range(len(arr) - 1):
# 		for j in range(i + 1, len(arr)):
# 			if arr[j] < arr[i]:
# 				tmp = arr[i]
# 				arr[i] = arr[j]
# 				arr[j] = tmp
# 	return arr

arr = list(range(10))
print(arr)
random.shuffle(arr)
print(arr)
print(selection_sort(arr))
