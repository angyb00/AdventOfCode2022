print("Part 1")
print("----------------------------------------------------------------")


priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
def calcScore(text):
    score = 0 
    mid = len(text) // 2
    first_half = list(set(text[:mid]))
    second_half = text[mid:]
    for i in range(len(first_half)):
        if first_half[i] in second_half:
            score += priorities.index(first_half[i]) + 1
    return score
    

total_score = 0 
with open("rucksack.txt", "r") as backpack:
    for line in backpack:
        total_score += calcScore(line.strip())

print(f"Sum is: {total_score}")
print("----------------------------------------------------------------")

