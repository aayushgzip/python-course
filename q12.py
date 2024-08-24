def remove_parenthesis(list1):
    list2 =[]
    for i in list1:
        while '(' in i  and ')' in i:
            start = i.index('(')
            end = i.index(')',start)
            i = i[:start] + i[end+1:]
        list2.append(i.strip())
    print(list2)
list1 = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
remove_parenthesis(list1)
