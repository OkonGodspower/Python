name = "Joseph"
age = 18
print("My name is", name)
print("I am", age, "years old")

subscribers = int(input("How many subscribers? "))

#if subscribers != 1000:
if subscribers >= 1000:
    print("Congratulations You've Been Monetized!")
elif subscribers >= 700:
    print("You're Almost there")
elif subscribers >= 500:
    print("You're Halfway there")
else:
    print("Keep building you're getting there")
    
    
views = [1200, 850, 3400, 560, 2100]
total = 0
for v in views:
    total = total + v
print(total)
print("Your average views is:", total / len(views))
#print(1200 + 850 + 3400 + 560 + 2100)
#print(len(views))
#print(8110 / 5)


fruits = ["mango", "orange", "banana", "pawpaw", "guava"]

print(fruits[0])    # mango (the first one)
print(fruits[4])    # guava (the last one)
print("There are",len(fruits), "fruits")  # 5 (how many items)
print("All the fruits without the fifth one are", len(fruits) - 1, "in number")
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

for fruit in fruits:   #loop (for)
    print("I like", fruit)
    
def double(n):
    return n * 2

answer = double(5)
print(answer)


def average(scores):
    total = 0
    for s in scores:
        total = total + s
    return total / len(scores)

result = average([1200, 850, 3400])
print(result)
print(total)
print(double(15))     # 30
print(double(100))   # 200
print(double(7))     # 14


numbers = [1, 2, 3, 4]

for x in numbers:
    print(double(x))
    
def courses(category):
    compulsory = ["Mathematics", "English", "Civic Education", "Data Processing"]
    science = ["Physics", "Chemistry", "Biology", "Agric", "Computer Science"]
    return compulsory + science
#for s in science: 
#    print("What is your", science, "score")