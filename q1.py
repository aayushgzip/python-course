def invertdict(dict):
    invert_dict={j:i for i,j in dict.items()}
    return invert_dict
dict1={1:"apple",2:"banana",3:"melon"}
print(dict1)
inverted = invertdict(dict1)
print(inverted)
