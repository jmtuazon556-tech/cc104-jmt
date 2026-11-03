def linear_search(items, target):
    # Iterate through the list using enumerate to get both index and value
    for index, value in enumerate(items):
        # Check if current value matches target
        if value == target:
            return index  # Return index when target is found
            
    # Return -1 if the loop finishes without finding the target
    return -1

# Test case matching the slide example
print(linear_search([10, 4, 12, 8], 12))  # Output: 2