print('Important NOTE:\n  Student score must be a number between 0 and 100')
student_score = input('Enter student score to get the grade: ')

# Check if input is a positive integer
if student_score.lstrip('-').isdigit():

    student_score = int(student_score)
    if 0 <= student_score <= 100:

        match student_score:
            case x if x > 90:
                Grade = 'A'
            case x if x > 80:
                Grade = 'B'
            case x if x > 70:
                Grade = 'C'
            case x if x > 60:
                Grade = 'D'
            case x if x > 50:
                Grade = 'E'
            case _:
                Grade = 'F'


        print(f"Student score is {student_score} and Grade is {Grade}")
    else:
        print("Student score entered is out of range... try again (0–100).")

else:
    print("Invalid input. Please enter a number only.")
