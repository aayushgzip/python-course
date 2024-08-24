my_file = 'C:\\Users\\Dell\\OneDrive\\Desktop\\osslab\\ass2\\python.txt'
char = []
with open(my_file, 'r') as file:
    content = file.readlines()
    char.extend(content)
print(char)
    
    
    
