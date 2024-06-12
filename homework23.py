# Second largest number in the list
# Write function that takes list of numbers, and returns the second largest number.
# If there's no second largest number in the list
# (empty list is passed, or list contains only the same number), function should return None.
# You should NOT use max/min built-n functions, sort/sorted.
# Write implementation that performs only one pass through the list (complexity O(n)).

def second_largest_number(lst):
    if len(lst) < 2:
        return None

    first = second = None
    for number in lst:
        if first is None or number > first:
            second = first
            first = number

        elif number != first and (second is None or number > second):
            second = number

    return second


print(second_largest_number([]))
print(second_largest_number([1, 1]))
print(second_largest_number([1, 2, 3, 4, 5]))

