# My Personal Details
name = "Eren"
age = 25.5
height = 1.76
student_now = True
city = "Poznan"

print(name, "is", age, "years old")
print(type(name), type(age))
print(type(height), type(student_now))

# Pizza Calculation
slices_per_student = 3
students = 15
enrolled_students = students + 3
present_students = enrolled_students - 2
total_slices_needed = present_students * slices_per_student
cost_per_student = 500 / present_students
boxes_to_order = total_slices_needed // 8
leftover_slices = (boxes_to_order*8) % present_students

print("There are" , present_students, "students present today" " and we need", total_slices_needed, "slices of pizza to feed everyone.")
print("Therefore, we need to order", boxes_to_order, "boxes of pizza and each student has to pay", cost_per_student, "zloty.")
print("There will be", leftover_slices, "slices of pizza left over after everyone has eaten.")