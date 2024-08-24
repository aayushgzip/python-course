my_string = input("enter string of numbers (eg 12,23,45,56)")
new_string = my_string.split(",")
print(new_string)
new_string = [int(x.strip()) for x in new_string]
print(new_string)
arr = list(map(lambda x: x*2, new_string))
print(arr)
