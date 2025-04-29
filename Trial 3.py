#While loop initial practice
while True:
    score =(input("Please give your score: "))
    if not score.isdigit():
        x=int(score)

        if x>=0 and x<=100:
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

            print("Input correct")
            break
        else:
            print("Input invalid")
            x = int(input("Please give your score: "))
