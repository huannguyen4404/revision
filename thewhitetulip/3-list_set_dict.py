list1 = [1, 3, 5]
list2 = list()
list = [1, '2', 1.11111, [1, 2, 3], 1]


tuple1 = (1, 2, 3, 4)
# tuple1[0] = 6 # TypeError: 'tuple' object does not support item assignment

set1 = {1, 2, 3, 4}
set2 = set(list1)
# a = set1[0] # TypeError: 'set' object does not support indexing
# c = set(list) # TypeError: unhashable type: 'list'

dict1 = dict()
dict2 = {'name': 'Henry', 'age': 32, 'country': 'Vietnam'}
dict2['class'] = 'ADC'
dict2['age'] = 18
print(dict2)


