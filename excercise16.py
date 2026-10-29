def closest_number(numbers, target):
    closest = numbers[0]
    for num in numbers: 
        current_distance = abs(num - target)
        closest_distance = abs(closest - target)


        if current_distance < closest_distance:
            closest = num
        elif current_distance == closest_distance:
            if num < closest:
                closest = num

    return closest

print(closest_number([4, 8, 15, 20], 13))
