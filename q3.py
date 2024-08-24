def n_largest(list1, N):
    n = len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j]<list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1[:N]
arr=[1,2,3,4,5,6,7,5,4,5,7,3,5,7,4,43,7,76,45,87,36]
print(arr)
n = int(input("enter value of N\n"))
new_arr = n_largest(arr, n)
print(new_arr)
        
        
        
