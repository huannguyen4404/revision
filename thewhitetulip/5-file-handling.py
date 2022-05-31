even_file = open('even.txt', 'w')
odd_file = open('odd.txt', 'w')

for i in range(100):
    if i % 2 == 0:
        even_file.write(str(i))
        even_file.write("\n")
    else:
        odd_file.write(str(i))
        odd_file.write("\n")

even_file.close()
odd_file.close()

print("Write files completed.")
print("Start to read files")

input_file = open("even.txt", "r")
lines = input_file.readlines()
# for line in lines:
#     print(line)

# print(lines)
lines = [line.strip() for line in lines]  # list comprehension
print(lines)
input_file.close()

file = open("even.txt", "a")
for i in range(100, 200):
    if i % 2 == 0:
        file.write(str(i) + "\n")
file.close()

# EXAMPLES
a = ["a.txt", "b.txt", "c.txt", "d.txt"]
b = [i.upper() for i in a]
print("Convert each element to upper case")
print(b)

b = [i.lower() for i in b]
print("Convert each element to lower case")
print(b)

a = [1, 3, 4, 5, 5]
print("filter values of list which are greater than 3")
b = [i for i in a if i > 3]
print(b)

a = ["Haskell", "Ruby", "Python"]
print("Display names which len > 3")
b = [i for i in a if len(i) > 3]
print(b)

a = [1, 3, 4, 5, 5]
print("Display even numbers")
b = [i for i in a if i % 2 == 0]
print(b)

# Exercise
name = input("give your name: ")
age = input("input your age: ")
height = input("height: ")

