def most_frequent(numbers):
    if not numbers:
        return None
    
    frequencies = {}
    for num in numbers:
        frequencies[num] = frequencies.get(num, 0) + 1
        
    max_freq = -1
    best_num = None
    
    for num, freq in frequencies.items():
        if freq > max_freq:
            max_freq = freq
            best_num = num
            
    return best_num

print(most_frequent([]))
