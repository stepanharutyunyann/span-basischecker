from functions import is_basis, is_span

def main():
    print("=== Vector Space Analyzer ===\n")
    print("What would you like to check?")
    print("1. Basis")
    print("2. Span")

    print("3. Exit\n")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            is_basis()
        elif choice == "2":
            is_span()
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()