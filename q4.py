string_maps = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
}
def product(n1, n2):
    str1 = string_maps[n1]
    str2 = string_maps[n2]
    prod = []
    for c1 in str1:
        for c2 in str2:
            prod.append(c1+c2)
    return prod        
            

def two_digit_combinations(n):
    if len(n) != 2:
        return "input must be two digit string"
    l1 = n[0]
    l2 = n[1]
    comb = product(l1, l2)
    return comb
    

digit_string = input("Enter a two-digit string: ")
result = two_digit_combinations(digit_string)
print("Possible combinations:", result)
