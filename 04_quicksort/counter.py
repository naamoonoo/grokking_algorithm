# def counter(arr):
# 	if len(arr) == 0:
# 		return 0
# 	arr.pop(0)
# 	return 1 + counter(arr)

def counter(arr):
	if arr == []:
		return 0
	return 1 + counter(arr[1:])

print(counter(list(range(20))))
