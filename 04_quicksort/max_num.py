import random

# def max_num(arr):
# 	if len(arr) == 0:
# 		return 0
# 	if len(arr) == 1:
# 		return arr[0]
# 	if arr[0] < arr[1]:
# 		arr[0] = arr[1]
# 	arr.pop(1)
# 	return max_num(arr)

def max_num(arr):
	if len(arr) == 2:
		return arr[0] if arr[0] > arr[1] else arr[1]
	sub_max = max_num(arr[1:])
	return arr[0] if arr[0] > sub_max else sub_max

arr = list(range(20))
random.shuffle(arr)
print(arr)
print(max_num(arr))
