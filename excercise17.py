def first_position(numbers, target):
    left = 0
    right = len(numbers) -1
    result = -1

    while left <= right:
        mid = ((left + right) // 2)

        if numbers[mid] == target:
            result = mid
            right = mid -1 
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid -1

    return result
print(first_position([1, 3, 5, 7], 6))