print('Important NOTE:\n  Student score must be a number between 0 and 100')
student_score = input('Enter student score to get the grade: ')

# Check if input is a positive integer
if student_score.lstrip('-').isdigit():

    student_score = int(student_score)
    if 0 <= student_score <= 100:

        if student_score > 90:
            Grade = 'A'
        elif student_score > 70:
            Grade = 'B'
        elif student_score > 50:
            Grade = 'C'
        elif student_score > 40:
            Grade = 'D'
        else:
            Grade = 'F'

        print(f"Student score is {student_score} and Grade is {Grade}")
    else:
        print("Student score entered is out of range... try again (0–100).")

else:
    print("Invalid input. Please enter a number only.")
