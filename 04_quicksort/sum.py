# def recursive_sum(arr):
# 	if len(arr) == 0:
# 		return 0
# 	if len(arr) == 1:
# 		return arr[0]
# 	return arr.pop(0) + recursive_sum(arr)

def recursive_sum(arr):
	if arr == []:
		return 0
	return arr[0] + recursive_sum(arr[1:])

arr = list(range(5))
print(recursive_sum(arr))
