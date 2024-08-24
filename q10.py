

def max_word(file):
    content = []
    with open(file_path,'r') as file:
        for line in file:
            content.extend(line.split())
    print(content)
    length = {}
    for i in content:
        if i in length.keys():
            length[i]+=1
        else:
            length[i]=1
    common_count = 0
    common_word = None
    for max_count, counter in length.items():
        if counter > common_count:
            common_word = max_count
            common_count = counter
    return common_word, common_count        
    
file_path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\osslab\\ass2\\python.txt'
max_word(file_path)
word, count = max_word(file_path)
print(f"\nmost common word is '{word}' with {count} occurences")

