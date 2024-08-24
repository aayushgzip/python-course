def iterative_binary(arr, low, high, x):
    while (low<=high):
        mid = low + (high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def recursive_binary(arr, low, high, x):
    if high>=low:
        mid = low + (high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            return recursive_binary(arr,mid+1,high,x)
        else:
            return recursive_binary(arr,low,mid-1,x)
    return -1    
if __name__=='__main__':
    arr = [20,13,24,54,41,57,34,56,]
    arr = sorted(arr)
    print(arr)
    x = int(input("enter value to search : "))
    pos = iterative_binary(arr,0,len(arr),x)
    pos2 = recursive_binary(arr,0,len(arr),x)
    if (pos != -1 and pos2 != -1):
        print(f"{x} is present at index {pos}")
    else:
        print("element not found")


            
