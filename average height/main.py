count = 0
height = 0

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    height = height + student_heights[n]
    count += 1

print(round(height/count))

# above is shown ay to not use sum()  len()
# with sum() and len() it could be like that:
#
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)
#
#
# another method:
#
# total_height = 0
# for height in student_heights:
#   total_height = total_height + height
#
# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1
#
# print(round(total_height/number_of_students))

