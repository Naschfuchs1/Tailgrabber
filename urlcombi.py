import itertools

words = [
    "Washed", "Frost", "Robot", "Misfits", "Shady", "Goat", "Rocked",
    "Skull", "Lives", "Handy", "Robot", "Chest", "Dawn", "Turkey", "Diet",
    "Parrot", "Chickens", "Locker", "Cannonball"
]

# Generate all permutations of 3-word combinations
combinations = itertools.permutations(words, 3)

# File path to store the results
output_file = "X:\\Users\\XXX\\Desktop\\combinationurls.txt"

# Iterate over the combinations and write them to the output file
with open(output_file, "w") as file:
    for combination in combinations:
        url = "https://what3words.com/" + ".".join(combination) + "\n"
        file.write(url)

print("Permutations written to", output_file)
