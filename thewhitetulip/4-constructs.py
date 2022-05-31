a = [1,2,3,4,[5,6,7]]
del a[0]
del a[3][2]
print(a)

a = {"IN":"India", "ES":"Espanol"}
key = 'IN'
del a[key]
a[key] = 'Indonesia'
print(a)
