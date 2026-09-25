from feedback import add_feedback
from analysis import show_analysis

def main():
    while True:
        print("\n===== MESS FEEDBACK ANALYZER =====")
        print("1. Add Feedback")
        print("2. View Analysis")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_feedback()
        elif choice == "2":
            show_analysis()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
