# Mess Feedback Analyzer

## 1. Introduction

Mess Feedback Analyzer is a simple Python console application made for collecting and checking feedback about mess food. A user can enter the name of a dish, give a rating from 1 to 5, and write a short comment.

The feedback is stored in a text file. The program can also display the saved feedback and calculate the average rating.

## 2. Problem Statement

Students often give feedback about mess food, but the feedback may not be organised in one place. This project provides a simple way to record food ratings and comments and check the overall rating.

## 3. Objectives

- To collect feedback about mess food.
- To allow users to give a rating from 1 to 5.
- To save feedback for later use.
- To display saved feedback.
- To calculate the average rating.

## 4. Features

- Add feedback for a dish.
- Enter a rating between 1 and 5.
- Add a comment about the food.
- Store feedback in a text file.
- View previously saved feedback.
- Calculate the average rating.
- Simple menu-based console interface.

## 5. Technologies Used

- Programming Language: Python
- Storage: Text file (`data.txt`)
- Editor: VS Code

## 6. How the Project Works

1. The user selects Add Feedback.
2. The user enters the dish name.
3. The user enters a rating from 1 to 5.
4. The user enters a comment.
5. The feedback is saved in `data.txt`.
6. The user can select View Analysis.
7. The program reads the saved feedback and calculates the average rating.

## 7. Example

Example input:

    Enter your choice: 1
    Enter dish name: Rice
    Enter rating (1-5): 4
    Enter your feedback: Good food

Example result:

    Feedback saved successfully

Analysis:

    ----- FEEDBACK -----
    Rice - 4 /5
    Comment: Good food

    Total reviews: 1
    Average rating: 4.0

## 8. Project Files

| File | Purpose |
|---|---|
| `main.py` | Controls the main menu and program flow |
| `feedback.py` | Takes feedback and saves it |
| `analysis.py` | Displays feedback and calculates the average |
| `data.txt` | Stores feedback records |
| `README.md` | Project documentation |
| `statement.md` | Project statement |

## 9. Testing

The project can be tested using different ratings and feedback.

- Test with a rating of 1.
- Test with a rating of 5.
- Add feedback for more than one dish.
- Check whether the average is calculated correctly.
- Enter a rating outside 1–5 and check the validation message.

## 10. Limitations

- It is a console-based application.
- Data is stored in a simple text file.
- It does not have a login system.
- It does not use a database.

## 11. Future Improvements

- Dish-wise average ratings.
- Date-wise feedback.
- Graphical user interface.
- Database storage.
- More detailed reports.

## 12. Conclusion

Mess Feedback Analyzer is a small Python project that demonstrates basic programming concepts such as functions, conditions, loops, user input, string handling, arithmetic operations, and file handling.
