def calculate_flames(name1, name2):
    flames = ['Friendship', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    total_chars = len(name1) + len(name2)
    common_chars = 0
    for char in name1:
        if char in name2:
            common_chars += 2
            name2 = name2.replace(char, "", 1)
    remaining_chars = total_chars - common_chars
    index = remaining_chars % len(flames)
    
    return flames[index]

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

result = calculate_flames(name1, name2)

# Output
print("Relationship between", name1, "and", name2, "is:", result)