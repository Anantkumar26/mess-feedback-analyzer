def show_analysis():
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No feedback available")
        return

    total = 0
    count = 0

    print("\n----- FEEDBACK -----")

    for line in lines:
        parts = line.strip().split("|")

        if len(parts) == 3:
            dish = parts[0]
            rating = int(parts[1])
            comment = parts[2]

            print(dish, "-", rating, "/5")
            print("Comment:", comment)

            total = total + rating
            count = count + 1

    average = total / count
    print("\nTotal reviews:", count)
    print("Average rating:", round(average, 2))
