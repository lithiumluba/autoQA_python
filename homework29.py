# TO DO: List linearization
# There's a list that could contain numbers and nested lists, that could contain numbers and nested lists,
# that could contain...
# Write function that takes list described above, and returns flat list consisting of all list elements.
# P.S You can't convert list to string, remove square brackets and split it back by whitespaces:)

def linearize_list(lst):
    result = []

    def flatten(sublist):
        for element in sublist:
            if isinstance(element, list):
                flatten(element)
            else:
                result.append(element)
    flatten(lst)

    return result


lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
print(linearize_list(lst))

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
