def insertion_sort(numbers):
    shifts = 0

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]  # Shifting element to the right
            shifts += 1                  # Increment counter for the shift
            j -= 1
            
        # Place the key at its correct sorted position
        numbers[j + 1] = key
        
    return numbers, shifts
print(inserion_sort([5, 3, 4]))

