def greet(name):
    print("Welcome to my Program", name)
    
greet("Joseph")
greet("Ada")


def average_of_two(a,b):
    print((a + b) / 2)
    
average_of_two(60, 80)


def average(scores):
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)

views = [1200, 850, 3400, 560, 2100]
result = average(views)
print("Average views:", round(result, 1))


def get_grade(avg):
    if avg >= 70:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"
    
print(get_grade(85))
print(get_grade(52))


year = int(input("Enter Year: "))
month = int(input("Enter Month: "))

print("calender".month(year))

