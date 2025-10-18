print("Grading System")

sub1 = float(input("Enter marks of subject 1: "))
sub2 = float(input("Enter marks of subject 2: "))
sub3 = float(input("Enter marks of subject 3: "))
sub4 = float(input("Enter marks of subject 4: "))
sub5 = float(input("Enter marks of subject 5: "))

average = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print("Average Marks:", average)

if 91 <= average <= 100:
    grade = "A1"
elif 81 <= average <= 90:
    grade = "A2"
elif 71 <= average <= 80:
    grade = "B1"
elif 61 <= average <= 70:
    grade = "B2"
elif 51 <= average <= 60:
    grade = "C1"
elif 41 <= average <= 50:
    grade = "C2"
elif 33 <= average <= 40:
    grade = "D"
elif 21 <= average <= 32:
    grade = "E1"
else: 
    grade = "E2"

print("Grade:", grade) 