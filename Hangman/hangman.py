import random

easy_words = [
    "apple", "banana", "grape", "orange", "house",
    "chair", "bread", "hello", "world", "school",
    "water", "happy", "smile", "green", "light",
    "music", "phone", "sleep", "dance", "river"
]

difficult_words = [
    "awkward", "bagpipes", "croquet", "dwarves", "fuchsia",
    "gizmo", "haiku", "injury", "jukebox", "knapsack",
    "larynx", "mnemonic", "nightclub", "ostracize", "pneumonia",
    "quartz", "rhubarb", "sphinx", "twelfth", "waltz"
]

difficulty = input("Difficulty? Easy or Hard (e/h): ").strip().lower()
if(difficulty == "e"):
    displayed = random.choice(easy_words).lower()
elif(difficulty == "h"):
    displayed = random.choice(difficult_words).lower()
else:
    print("Please enter a correct value..\nEXITING")
    exit()
guessed = []
def get_displayed(displayed, guessed):
    return ' '.join([char if char in guessed else '_' for char in displayed])

print("Word to guess:", get_displayed(displayed, guessed))


running = True
while running:
    character = input("Guess a letter: ").strip().lower()

    if not character or len(character) != 1:
        print("Please enter exactly one letter..")
        continue
    
    if character in guessed:
        print(f"You've already guesses '{character}'")
        continue

    if character in displayed:
        guessed.append(character)
        print("Correct!")
    else:
        print(f"Nope! {character} is not in the word..")
        continue

    current_display = get_displayed(displayed, guessed)
    print("Word:",{current_display})

    if '_' not in current_display:
        print("You guessed the word!\nThe word was:", displayed)
        running = False