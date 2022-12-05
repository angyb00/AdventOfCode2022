#print("Part 1")
#print("----------------------------------------------------------------")


"""
A -> Rock 
B -> Paper 
C -> Scissor

X -> Rock (1 pts)
Y -> Paper (2 pts)
Z -> Scissor (3 pts)

Loss -> 0 pts
Tie -> 3 pts
Win -> 6 pts 

9 Total Combinations
"""
score_combination = {1: "B X", 4: "A X", 7: "C X", 2: "C Y", 5: "B Y", 
8: "A Y", 3: "A Z", 6: "C Z", 9: "B Z"}


def compute_score(match):   #return val only not list
    return [k for k, v in score_combination.items() if v == match.strip()][0]
    
    

total_score = 0 
with open("strategy.txt", "r") as strategies:
    for strategy in strategies:
        total_score += compute_score(strategy)
        

print(f"Total score: {total_score}")

print("----------------------------------------------------------------")
print("Part 2")    
print("----------------------------------------------------------------")





print("----------------------------------------------------------------")