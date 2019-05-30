def binary_search(list, item):
	low = 0
	high = len(list) - 1
	# step = 1
	while low <= high:
		mid = (high + low) / 2
		guess = list[mid]
		# print("{0} step\n".format(step))
		# step += 1
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1

	return None

my_list = list(range(1, 50))
print(binary_search(my_list, 23))
