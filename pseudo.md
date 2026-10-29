        EXCERCISE 15
FUNCTION most_frequent(numbers):
    IF numbers is empty THEN
        RETURN None
    END IF

    // Step 1: Track counts while preserving first-appearance order
    CREATE an empty dictionary called frequencies

    FOR EACH num IN numbers:
        IF num exists in frequencies THEN
            INCREMENT frequencies[num] by 1
        ELSE
            SET frequencies[num] to 1
        END IF
    END FOR

    // Step 2: Find the highest frequency
    best_num to None
    max_freq to -1

    FOR EACH (num, count) IN frequencies:
        // Using strict greater-than (>) ensures that if counts are equal,
        // the one that was inserted first (earlier in the list) is kept.
        IF count > max_freq THEN
            SET max_freq to freq
            SET best_num to num
        END IF
    END FOR

    RETURN best_num





EXCERCISE 16
    FUNCTION closest_number(numbers, target)
    SET closest TO numbers[0]
    
    FOR EACH num IN numbers DO
        SET current_distance TO absolute_value_of(num - target)
        SET closest_distance TO absolute_value_of(closest - target)
        
        IF current_distance IS LESS THAN closest_distance THEN
            SET closest TO num
        ELSE IF current_distance IS EQUAL TO closest_distance THEN
            IF num IS LESS THAN closest THEN
                SET closest TO num
            END IF
        END IF
    END FOR
    
    RETURN closest
END FUNCTION





EXCERCISE 17
Function first_position(numbers, target):
    Set left = 0
    Set right = length(numbers) - 1
    Set result = -1

    While left <= right:
        Set mid = floor((left + right) / 2)

        If numbers[mid] == target:
            Set result = mid
            Set right = mid - 1   // Keep looking for an earlier occurrence on the left
        Else If numbers[mid] < target:
            Set left = mid + 1
        Else:
            Set right = mid - 1

    Return result

EXCERCISE 18
FUNCTION insertion_sort(numbers)
    SET shifts TO 0
    
    FOR i FROM 1 TO length(numbers) - 1 DO
        SET key TO numbers[i]
        SET j TO i - 1
        
        WHILE j >= 0 AND numbers[j] > key DO
            SET numbers[j + 1] TO numbers[j]  // Shift element to the right
            INCREMENT shifts BY 1             // Track the shift
            SET j TO j - 1
        END WHILE
        
        SET numbers[j + 1] TO key             // Insert key into correct position
    END FOR
    
    RETURN numbers, shifts
END FUNCTION


Excercise 19
FUNCTION count_leaves(root)
    // Step 1: Does this node exist?
    IF root IS NULL THEN
        RETURN 0
    END IF

    // Step 2: Does it have a left child or right child?
    IF root.left IS NULL AND root.right IS NULL THEN
        RETURN 1
    END IF

    // Step 3: Check the left and right parts of the tree recursively
    RETURN count_leaves(root.left) + count_leaves(root.right)
END FUNCTION

