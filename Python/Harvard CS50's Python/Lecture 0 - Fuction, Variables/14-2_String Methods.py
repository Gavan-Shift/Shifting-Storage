# Ask user for their name
name = input("What's your name?")

# Remove whitespace from str + Capitalize the first letter of the user's nameading/trailing whitespace
name = name.strip().capitalize()

# Say hello to user
print(f"hello, {name}")