import os


working_dir = os.getcwd()
input_file = working_dir + "\\input.txt"

with open(file=input_file) as raw_inventory:
    inventory = raw_inventory.read()

inv_dict = {}
split_inventory = inventory.split("\n")

counter = 0
elves_inventory = {counter: []}
for calorie in split_inventory:
    try:
        calorie = int(calorie)
        if calorie > 0:
            elves_inventory[counter].append(calorie)
    except Exception:
        counter += 1
        elves_inventory[counter] = []

calories_list = []
for backpack in elves_inventory:
    calories_in_backpack = sum(elves_inventory[backpack])
    calories_list.append(calories_in_backpack)

print("Calories list in backpacks: %s" % calories_list)
biggest_calories_sum = max(calories_list)
print("\nElf with most calories is carrying: %s" % biggest_calories_sum)

# Part Two
sorted_calories_list = sorted(calories_list, reverse=True)
print("Top 3 elves: " + str(sorted_calories_list[:3]))
print("Top 3 elves total calories: %s" % sum(sorted_calories_list[:3]))
