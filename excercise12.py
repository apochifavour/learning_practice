def move_zeros(numbers):     
    position = 0          
    
    for i in range(len(numbers)):         
        if numbers[i] != 0:             
            numbers[position] = numbers[i]             
            position += 1                  
    
    for i in range(position, len(numbers)):         
        numbers[i] = 0  
        
    return numbers  
num = move_zeros([0, 1, 0, 3, 12])
print(num)




def move_zeros(numbers):
    non_zero_pos = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[non_zero_pos] = numbers[i]
            non_zero_pos += 1
            
    for i in range(non_zero_pos, len(numbers)):
        numbers[i] = 0

    return numbers 
num = move_zeros([0, 1, 0, 3, 12])
print(num)






































"""def move_zeros(numbers):
    non_zero_pos = 0[]
    
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[non_zero_pos] = numbers[i]
            non_zero_pos += 1
            
    for i in range(non_zero_pos, len(numbers)):
        numbers[i] = 0

num = move_zeros([0, 1, 0, 3, 12])5
print(num)"""


"""def move_zeros(numbers):     
    non_zero_pos = 0          
    
    for i in range(len(numbers)):         
        if numbers[i] != 0:             
            numbers[non_zero_pos] = numbers[i]             
            non_zero_pos += 1                  
    
    for i in range(non_zero_pos, len(numbers)):         
        numbers[i] = 0  
        
    return numbers  
num = move_zeros([0, 1, 0, 3, 12])
print(num)"""





