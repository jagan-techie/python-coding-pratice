# 1. Reverse an Array
# Problem: Reverse the order of elements in an array.
# Python Trick: You can achieve this instantly using slicing ([::-1]) or modify it in place with .reverse()


def reverse_array(arr):
    # In-place reversal
    arr.reverse()
    return arr

# Example
print(reverse_array([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
