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

# Part 2:
