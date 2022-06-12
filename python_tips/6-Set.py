some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

duplicates = set([x for x in some_list if some_list.count(x) > 1])

print("duplicates:", duplicates)

valid = {'yellow', 'red', 'blue', 'green', 'black'}
input_set = set(['red', 'brown'])
print("intersection:", input_set.intersection(valid))
print("difference:", input_set.difference(valid))

