def valuesort(dict1):
    arr = []
    for i in dict1:
        arr.append(i)
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    new_dict={}
    for i in arr:
        new_dict.update({i:dict1[i]})
    return new_dict
dict1= {21:"apple",11:"banana",41:"orange",7:"mango"}
print(dict1)
sorted_dict=valuesort(dict1)
print(sorted_dict)
