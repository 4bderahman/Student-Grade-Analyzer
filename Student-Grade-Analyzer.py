n = int(input("Enter the number of students: "))

notes = []
moyenne = 10

for i in range(n):
    note = float(input(f"Enter the grade of student {i + 1}: "))
    notes.append(note)

print("Grades higher than the average are:")
for i in notes:
    if i > moyenne:
        print(i)
