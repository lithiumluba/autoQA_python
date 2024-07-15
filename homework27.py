 # TO DO: Write generator function that takes two arguments:
 # lst - list
 # iter_num - integer with default value None
 # Generator should return items from the list one by one.
 # When generator comes to the last item, it should start from the beginning and repeat it iter_num times.
 # If iter_num is None, generator should return items infinitely

def list_item_generator(lst, iter_num=None):
    while iter_num is None or iter_num > 0:
        for item in lst:
            yield item
        if iter_num is not None:
            iter_num -= 1
print('Normal Example')
lst = ['a', 'b']
for i in list_item_generator(lst, iter_num=2):
    print(i)

print('Infinite Loop Example with break condition to prevent an infinite loop  ')
lst = ['a', 'b']
for i in list_item_generator(lst):
    print(i)
    if i == 'b':
        break
