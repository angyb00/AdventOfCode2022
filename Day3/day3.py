print("Part 1")
print("----------------------------------------------------------------")

# index + 1 corralates with the priority of the letter 
priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
def calcScore(text):
    score = 0 
    mid = len(text) // 2
    first_half = list(set(text[:mid]))
    second_half = text[mid:]
    for letter in first_half:
        if letter in second_half:
            score += priorities.index(letter) + 1
    return score
    

total_score = 0 
with open("rucksack.txt", "r") as backpack:
    for line in backpack:
        total_score += calcScore(line.strip())


print(f"Sum is: {total_score}")
print("----------------------------------------------------------------")


print("Part 2")    
print("----------------------------------------------------------------")


def calcSum(group):
    sum = 0
    match = list(set(group[0]))
    for letter in match:
        if letter in group[1] and letter in group[2]:
            sum += priorities.index(letter) + 1
    return sum  
            
        
    
total_sum = 0
# read in 3 lines at a time since that constitutes a group
with open("rucksack.txt", "r") as backpack:
    group = []
    elfs_per_group = 3
    for line in backpack:
        group.append(line.strip())
        if len(group) >= elfs_per_group:
            total_sum += calcSum(group)
            group = []
        
print(f"Total sum is: {total_sum}")

print("----------------------------------------------------------------")
