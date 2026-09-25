def add_feedback():
    dish = input("Enter dish name: ")
    rating = int(input("Enter rating (1-5): "))

    if rating < 1 or rating > 5:
        print("Please enter rating between 1 and 5")
        return

    comment = input("Enter your feedback: ")

    file = open("data.txt", "a")
    file.write(dish + "|" + str(rating) + "|" + comment + "\n")
    file.close()

    print("Feedback saved successfully")
