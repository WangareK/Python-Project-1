student_name = input("Please enter your name: ")
student_id = input("Please enter your student ID: ")
# if student_id == "":
#     print("Please provide a student ID")
# else:
#     score= input("Please enter your score: ")
# x = int(score)
# Grade = " "
while True:
    score =(input("Please give your score: "))
    if not score.isdigit():
        print("Input must be a number")
        continue
    x=int(score)
    if x<0  or x>100:
        print("Input should be within 1-100 range")
        continue
    if x > 90:
        Grade = "A"
        Remark = "Exemplary"
    elif 80 <= x < 90:
        Grade = "B+"
        Remark = "Very Good"
    elif 70 <= x < 80:
        Grade = "B"
        Remark = "Good"
    elif 60 <= x < 70:
        Grade = "C"
        Remark = "Satisfactory"
    elif 50 <= x < 60:
        Grade = "D"
        Remark = "Average"
    else:
        Grade = "F"
        Remark = "Fail"
        print(f"Your score is {x} Grade {Grade} and this performance is {Remark}")

    print(f"Your score is {x} Grade {Grade} and this performance is {Remark}")
    break
# else:
#     print("Input invalid")
#     x = int(input("Please give your score: "))
