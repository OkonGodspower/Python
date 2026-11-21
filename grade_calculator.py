print("STUDENT GRADE CALCULATOR")

name = input("Enter your name: ")

print("Science = 1", "Art = 2",  "Commercial = 3")
course = input("Enter your Course: ")



maths = float(input("Enter your Mathematics Score: "))
english = float(input("Ednter your English Score: "))
cs = float(input("Enter your Computer Science Score: "))
phy = float(input("Enter your Physics Score: "))
chem = float(input("Enter your Chemistry Score: "))
bio = float(input("Enter your Biology Score: "))
civic = float(input("Enter your Civic Education Score: "))
agric = float(input("Enter your Agricultural Science Score: "))
crs = float(input("Enter your Christian Religious Studies Score: "))
geo = float(input("Enter your Geography Score: "))
lit = float(input("Enter your Literature-in-English Score: "))
gov = float(input("Enter your Government Score: "))
econ = float(input("Enter your Economics Score: "))
finacc = float(input("Enter your Financial Accounting Score: "))
mak = float(input("Enter your Marketing Score: "))
com = float(input("Enter your Commerce Score: "))

science = [maths, english, civic, crs, cs, phy, chem, bio, geo, agric]
art = [maths, english, civic, crs, cs, lit, gov, econ, agric]
commercial = [maths, english, civic, cs, crs, finacc, mak, com, econ]

for s in science:
    float(input("Enter your", science, "Score: "))
print(science)

if course == science:
    print(science)
elif course == art:
    print(art)
elif course == commercial:
    print(commercial)
else:
    print("Pick a course you MOTHER FUCKER")
    
print(science)
print(art)
print(commercial)

total = int(maths + english + cs + phy + chem)
#total = maths + english + cs + phy + chem
average = float(maths + english + cs + phy + chem) / 5
#average = total / 5
 
 
print("Student:", name)
print("Maths:", maths)
print("English:", english)
print("Computer Science:",cs)
print("Student:", name)
print("Total Score:", total)
print("Average:", round(average, 3))

if total >= 450:
    print("Grade: A")
elif total >= 380:
    print("Grade: B")
elif total >= 350:
    print("Grade: C")
elif total >= 300:
    print("Grade: D")
elif total >= 250:
    print("Grade: E")
else :
    print("Grade: F")
    
#if average >= 70:
#    grade = "A"
#elif average >= 60:
#    grade = "B"
#elif average >= 50:
#    grade = "C"
#elif average >= 45:
#   grade = "D"
#elif average >= 40:
#    grade = "E"
#else:
#    grade = "F" 

#print("Grade:", grade)
    
if total >= 140:
    print("Result: PASS")
else :
    print("Result: FAIL")