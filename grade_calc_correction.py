def get_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


print("STUDENT GRADE CALCULATOR")

name = input("Enter your name: ")
stream = input("Which course are you studying? (science / art / commercial): ").lower()

if stream == "science":
    subjects = ["Mathematics", "Physics", "Chemistry", "Biology", "English"]
elif stream == "art":
    subjects = ["Literature", "Government", "History", "CRK", "English"]
elif stream == "commercial":
    subjects = ["Accounting", "Economics", "Commerce", "Business Studies", "English"]
else:
    print("Invalid choice. Please run the program again.")
    exit()

total = 0
for subject in subjects:
    score = float(input("Enter your " + subject + " score: "))
    total = total + score

average = total / len(subjects)
grade = get_grade(average)

print("Student:", name)
print("Course:", stream)
print("Total Score:", total)
print("Average:", round(average, 1))
print("Grade:", grade)

if grade == "F":
    print("Result: FAIL")
else:
    print("Result: PASS")