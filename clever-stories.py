# Creativity added: This program automatically chooses whether to use "a" or "an" before the adjective based on the first letter, making the story sound more natural.

# Prompt the user for words
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")

# Automatically capitalize the exclamation
exclamation = exclamation.capitalize()

# Determine whether to use "a" or "an"
if adjective[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"

# Display the story
print("\nYour story is:\n")

print("The other day, I was really in trouble. It all started when I saw", article)
print(f"{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3}")
print("right in front of my family.")