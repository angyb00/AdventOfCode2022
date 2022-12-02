import heapq

# Part 1 

"""

Heap useful for part 2 so multiply all elf calories to create max heap

"""
print("Part 1")
print("----------------------------------------------------------------")

calorie_list = []
individual_elf = 0 
with open("calories.txt", "r") as calories: 
    for calorie in calories:
        if calorie == '\n':
            calorie_list.append(individual_elf)
            individual_elf = 0 
        else: 
            individual_elf += int(calorie) * -1 

print(f"Elf with most calories has: {min(calorie_list) * -1}")
print("----------------------------------------------------------------")


#part 2 
print("Part 2")    
print("----------------------------------------------------------------")
top_three = 0 
heapq.heapify(calorie_list)

for i in range(3):
    smallest = heapq.heappop(calorie_list)
    top_three += smallest
    

print(f"Combined calories of the top 3 elves is: {top_three * -1}")
print("----------------------------------------------------------------")
calories.close() 