# Write function lst2dict(lst) that takes list and returns dictionary.
# Dictionary should contain key-value pairs, where
# - key is list element on even position (0, 2, 4, ...)
# - value corresponding to this key is the list element, following after key
# If list has odd length, last item shouldn't be taken into account.

def lst2dict(lst):
    result = {}
    for _ in range(0, len(lst) - 1, 2):
        result[lst[_]] = lst[_ + 1]
    return result


print(lst2dict([0, 1, 2, 3, 4]))
print(lst2dict(['a', 'A', 'b', 'B', 'c']))
print(lst2dict([]))
print(lst2dict([1]))

