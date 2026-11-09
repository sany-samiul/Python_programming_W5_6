
def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")


def askChoice():
    choice = input("Your choice: ")

    try:
        return int(choice)
    except ValueError:
        print("Unknown option!")
        return -1


def main():
    print("Program starting.")

    count = 0

    while True:
        showOptions()
        choice = askChoice()

        if choice == 1:
            print(f"Current count - {count}")

        elif choice == 2:
            count += 1
            print("Count increased!")

        elif choice == 3:
            count = 0
            print("Cleared count!")

        elif choice == 0:
            print("Exiting program.")
            print()
            break

        elif choice == -1:
            pass

        else:
            print("Unknown option!")

        print()

    print("Program ending.")


# Start the program when the file is imported
main()
