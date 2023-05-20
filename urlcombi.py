import itertools

words = [
    "Washed", "Frost", "Robot", "Misfits", "Shady", "Goat", "Rocked", "Skull", "Lives",
    "Handy", "Robot", "Chest", "Dawn", "Turkey", "Diet", "Parrot", "Chickens", "Locker",
    "Cannonball"
]

combinations = itertools.combinations(words, 3)

output_path = r"X:\Users\XXX\Desktop\123.txt"

with open(output_path, "w") as file:
    for combination in combinations:
        if len(set(combination)) == 3:
            file.write("https://what3words.com/" + ".".join(combination) + "\n")

print(f"File created at: {output_path}")
