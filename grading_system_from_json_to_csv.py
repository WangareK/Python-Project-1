import json
import csv
import os               #operating system module to check if files exist or if files are empty


class Student:
    # List of subjects
    SUBJECTS = ['Math', 'English', 'Kiswahili', 'Science', 'Social Studies']

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        # creates a dictionary with a key-value pair with subject name as key and none as value, grades not ye assigned
        self.grades = {subject: None for subject in self.SUBJECTS}


    # Convert score to grade
    def assign_grade(self, score):
        if score is None:
            return "N/A"        #if no score has been assigned return not applicable
        elif score >= 90:
            return "A"
        elif score >= 80:
            return "A-"
        elif score >= 70:
            return "B+"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C+"
        elif score >= 40:
            return "C"
        elif score >= 30:
            return "D+"
        elif score >= 20:
            return "D"
        else:
            return "F"


class GradingSystem:
    def __init__(self):
        self.students = {}
        self.json_file = 'students.json'
        self.csv_file = 'grades.csv'
        self.load_data()                          #read data from json file


    # Load student data from JSON file
    def load_data(self):
        try:        #try block checks for any errors in the block of code
                     #check if the json file exists, checks if the file has content(not empty)
            if os.path.exists(self.json_file) and os.path.getsize(self.json_file) > 0:
                with open(self.json_file, 'r') as file:         #open json file in read mode
                    data = json.load(file)                      #parse into python dictionary
                    for student_data in data:
                        student_id = student_data["student_id"]
                        student = Student(student_id, student_data["name"])     #create student object with name and ID
                        student.grades = student_data["grades"]                 #set grades dictionary
                        self.students[student_id] = student                     #sets up student in students dict using student_id
                print(f"Loaded {len(self.students)} students.")             #reports how many students successfully onboarded
            else:
                print("No student data found.")                         #if file doesn't exist or is empty
        except Exception as e:
            print(f"FileNotFoundError: {e}")           #if any other error occurs(broad error statements hide the real issue)
            self.students = {}                      #to allow programme to run, initialise as empty
        except json.JSONDecodeError as e:           #if json file contains invalid syntax, malformed data
            print(f"Error decoding JSON: {e}")
            self.students = {}


    #Save student data to JSON file
    def save_data(self):
        data = []
        for student in self.students.values():
            data.append({                           #build a list of dictionaries for each student
                "student_id": student.student_id,
                "name": student.name,
                "grades": student.grades
            })

        with open(self.json_file, 'w') as file:         #opens json file in write mode
            json.dump(data, file, indent=4)              #writes to json file
        print("Data saved successfully.")

    # Export student grades to CSV file
    def export_to_csv(self):
        with open(self.csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write header
            header = ['Student ID', 'Name']        #adds csv header row, two columns
            for subject in Student.SUBJECTS:
                header.extend([f"{subject} Score", f"{subject} Grade"])         #adds two columns foe each subject
            writer.writerow(header)                                              #first row in csv file

            # Write student data
            for student in self.students.values():
                row = [student.student_id, student.name]    #add student_id and name

                # Add subject scores and grades
                for subject in Student.SUBJECTS:
                    score = student.grades[subject]
                    row.append(score if score is not None else "N/A")           #adds score
                    row.append(student.assign_grade(score))                 #adds grades

                writer.writerow(row)                #writes the data as row in csv

        print(f"Grades exported to {self.csv_file}")


    #Auto generate student ID
    def generate_id(self):
        if not self.students:
            return "STU001"

        # Get the highest existing ID number
        # ids = [int(sid[3:]) for sid in self.students.keys()]
        ids = []
        for sid in self.students.keys():        #list with all student IDs
            number_part = int(sid[3:])          #substring starting from the 4th character,extracts the number part only
            ids.append(number_part)             #gathers all integers in a list
        next_num = max(ids) + 1                 #finds highest number in list and adds one
        return f"STU{next_num:03d}"             #generates new ID that is one number higher and formated to 3 digit

    #Add a new student
    def add_student(self):
        name = input("Enter student name: ")
        if not name.strip():        #if condition true, user did not input any non-whitespace characters, returns error
            print("Error: Name cannot be empty.")       #should be no whitespaces
            return

        student_id = self.generate_id()
        student = Student(student_id, name)                 #object with student id and name
        self.students[student_id] = student  #adds object to students dictionary in grading system (student_id is the key)
        print(f"Added student {name} with ID: {student_id}")

        # Ask if user wants to enter grades now
        choice = input("Enter grades now? (y/n): ").lower()   #converts input to lowercase
        if choice == 'y':               #if condition y met, proceeds to next line
            self.enter_grades(student_id)   #passes student id allowing input of specific student

    # Enter or edit grades for a student
    def enter_grades(self, student_id):
        student = self.students.get(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return

        print(f"\nEntering grades for {student.name} (ID: {student_id})")
        for subject in Student.SUBJECTS:     #grade for specific subject
            current = student.grades[subject]
            prompt = f"{subject} grade" + (f" (current: {current})" if current is not None else "")
            #prompt string for user, appends current grade

            while True:
                grade_input = input(f"{prompt}: ")      #prompt to enter grade until valid input received
                if not grade_input:  # Skip if empty
                    break

                try:
                    grade = float(grade_input)          #floating point number
                    if 0 <= grade <= 100:
                        student.grades[subject] = grade     #assigns score to corresponding subject
                        letter = student.assign_grade(grade)        #assigns letter grade
                        print(f"Recorded {grade} ({letter}) for {subject}")
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number.")           #ValueError if input cannot be converted to float

    # List all students
    def list_students(self):
        if not self.students:       #checks if dictionary is empty
            print("No students found.")
            return []
        print("\nSTUDENT LIST:")
        print("-" * 80)     #prints separator line, visual separation with 50hyphens
        header = f"{'ID':<8} {'Name':<20}"          #prints column titles with width formatting.
        for subject in Student.SUBJECTS:
            header += f"{subject:<12}"
        print(header)
        print("-" * 80)         #another separator line

        student_list = []
        for student_id, student in sorted(self.students.items()):   #iterates through student list, sorted by student ID
            row = f"{student_id:<8} {student.name:<20}"
            for subject in Student.SUBJECTS:        #iterates through each subject getting the score
                score = student.grades.get(subject)
                if score is not None:
                    letter = student.assign_grade(score)
                    row += f"{score}({letter})     "
                else:
                    row += "N/A           " #if no score prints N/A
            print(row)
            student_list.append(student_id)

        return student_list


    # View detailed grades for a student
    def view_student(self, student_id):
        student = self.students.get(student_id)
        if not student:
            print(f"Student with ID {student_id} not found.")
            return

        print(f"\nGRADES FOR: {student.name} (ID: {student_id})")
        print("-" * 40)
        print(f"{'Subject':<15} {'Score':<8} {'Grade':<5}")
        print("-" * 40)

        for subject in Student.SUBJECTS:
            score = student.grades[subject]
            grade = student.assign_grade(score)
            score_display = score if score is not None else "N/A"
            print(f"{subject:<15} {score_display:<8} {grade:<5}")


    def display_menu(self):
        print("\n===== STUDENT GRADING SYSTEM =====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. View Student Details")
        print("4. Enter/Edit Grades")
        print("5. Export to CSV")
        print("6. Save and Exit")
        return input("Enter your choice (1-6): ")


def main():
    print("Welcome to Student Grading System")
    system = GradingSystem()

    while True:
        choice = system.display_menu()

        if choice == '1':  # Add student
            system.add_student()
            system.save_data()

        elif choice == '2':  # List students
            system.list_students()

        elif choice == '3':  # View student details
            students = system.list_students()
            if students:
                student_id = input("\nEnter student ID to view: ")
                system.view_student(student_id)

        elif choice == '4':  # Enter/edit grades
            students = system.list_students()
            if students:
                student_id = input("\nEnter student ID to edit grades: ")
                system.enter_grades(student_id)
                system.save_data()

        elif choice == '5':  # Export to CSV
            system.export_to_csv()

        elif choice == '6':  # Save and exit
            system.save_data()
            print("Thank you for using Student Grading System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

