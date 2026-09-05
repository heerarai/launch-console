print("Welcome to my personal console!")

name = input("What is your name? ")

print(f"Nice to meet you, {name}!")

while True:
    print("\nMenu:")
    print("1. About me")
    print("2. My goals")
    print("3. Fun fact")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("I am a high school student interested in technology, engineering, and research.")

    elif choice == "2":
        print("My goals are to succeed in college, explore engineering, and build projects that help people.")

    elif choice == "3":
        print("Fun fact: I have volunteered for more than 250 hours!")

    elif choice == "4":
        print(f"Goodbye, {name}! Thanks for stopping by.")
        break

    else:
        print("Please enter a valid number from 1 to 4.")