import string
import os

# Part 1:
input_file = str(os.getcwd()) + "\\input.txt"

with open(file=input_file) as raw_input:
    rucksacks = raw_input.read().splitlines()


def return_item_priority(item):
    letters = string.ascii_letters
    priority = letters.index(item) + 1  # Range is 1-52, so it's equal to letter's index + 1
    return priority


def return_item_from_both_compartments(compartment_a, compartment_b):
    list_compartment_a = []
    list_compartment_b = []
    list_compartment_a[:0] = compartment_a  # split the string into a list of it's characters
    list_compartment_b[:0] = compartment_b  # split the string into a list of it's characters
    items_in_first_compartment = list_compartment_a
    items_in_second_compartment = list_compartment_b
    print("Items in rucksacks: " +
          str(items_in_first_compartment),
          str(items_in_second_compartment))
    for item in items_in_first_compartment:
        if item in items_in_second_compartment:
            print("Found a matching item: %s" % item)
            return item


matching_items_priorities = []
for rucksack in rucksacks:
    try:
        slice_in_half = slice(int(len(rucksack) / 2))  # Every string is dividable by two
        first_half = rucksack[slice_in_half]
        second_half = rucksack.split(sep=first_half, maxsplit=1)[1]
        assert first_half + second_half == rucksack
        matching_item = return_item_from_both_compartments(compartment_a=first_half,
                                                           compartment_b=second_half)
        matching_items_priorities.append(return_item_priority(item=matching_item))
        print("")
    except BaseException:
        print("Stripping failed")

print("Sum of priorities for matching items: %s" % sum(matching_items_priorities))
print("\nEnd of Part 1\n")

# Part 2:


def find_matching_item_in_group(group_rucksacks):
    print(group_rucksacks)
    list_rucksack_a, list_rucksack_b, list_rucksack_c = [], [], []
    list_rucksack_a[:0] = group_rucksacks[0]  # split the string into a list of it's characters
    list_rucksack_b[:0] = group_rucksacks[1]  # split the string into a list of it's characters
    list_rucksack_c[:0] = group_rucksacks[2]  # split the string into a list of it's characters
    for item in list_rucksack_a:
        if item in list_rucksack_b and item in list_rucksack_c:
            print("Found a matching item: %s" % item)
            return item


print(rucksacks)
dict_elements_counter = 0
groups = {dict_elements_counter: []}
elf_counter = 0
for rucksack in rucksacks:
    elf_counter += 1
    if elf_counter <= 3:
        groups[dict_elements_counter].append(rucksack)
    else:
        dict_elements_counter += 1
        groups[dict_elements_counter] = []
        groups[dict_elements_counter].append(rucksack)
        elf_counter = 1
print(groups)

group_items_priority_list = []
group_counter = 0
for group in groups:
    group_matching_item = find_matching_item_in_group(group_rucksacks=groups[group_counter])
    item_priority = return_item_priority(item=group_matching_item)
    group_items_priority_list.append(item_priority)
    group_counter += 1

print("Sum of the priorities for item types is: %s" % sum(group_items_priority_list))
