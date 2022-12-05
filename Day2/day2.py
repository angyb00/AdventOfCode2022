print("Part 1")
print("----------------------------------------------------------------")

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
# Look up table 
score_combination = {
1: "B X", 
4: "A X",
7: "C X",
2: "C Y",
5: "B Y",
8: "A Y",
3: "A Z",
6: "C Z",
9: "B Z"
}


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

"""
X -> Lose 
Y -> Draw 
Z -> Win
"""

total_score = 0
scores = {} 

#Match requires Python 3.10 or newer
#Create new commbinations based off the conditions and use our compute score function
def create_combination(line):
    condition = line[2]
    opponent_choice = line[0]
    player_choice = " " + line[2]
    match condition:
        case "X":
            if opponent_choice == "A":
                player_choice = " Z"
            elif opponent_choice == "C":
                player_choice = " Y"
        case "Y":
            if opponent_choice == "A":
                player_choice = " X"
            elif opponent_choice == "C":
                player_choice = " Z"
        case "Z":
            if opponent_choice == "A":
                player_choice = " Y"
            elif opponent_choice == "C":
                player_choice = " X"
        case _:
            return "Error"
    return opponent_choice + player_choice


with open("strategy.txt", "r") as strategies:
    for strategy in strategies:
        new_combo = create_combination(strategy.strip())
        total_score += compute_score(new_combo)
       

print(f"Total score: {total_score}")
print("----------------------------------------------------------------")