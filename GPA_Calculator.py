print("\n")  # For new line
print("****** Welcome to the GPA Calculator App! ******")
print("Caution: Marks must be greater than 0 and less than or equal to 100.")
print("\n")  # For new line


# user's input for the marks of the 4 subjects (bengali, english, math, science)
bengali_marks = int(input("Enter your obtained marks in Bengali: "))
english_marks = int(input("Enter your obtained marks in English: "))
math_marks = int(input("Enter your obtained marks in Math: "))
science_marks = int(input("Enter your obtained marks in Science: "))


# Define function for calculate the average of the marks of the 4 subjects (bengali, english, math, science)
def calculate_average(bengali_marks, english_marks, math_marks, science_marks):
    total_marks = bengali_marks + english_marks + math_marks + science_marks
    average_marks = total_marks / 4
    return average_marks


# Define function for calculate the Grade using the average of the marks of the 4 subjects (bengali, english, math, science)
def calculate_grade(average_marks):
    if 91 <= average_marks <= 100:
        grade = "A+"
    elif average_marks >= 71:
        grade = "A"
    elif average_marks >= 61:
        grade = "B"
    elif average_marks >= 51:
        grade = "C"
    elif average_marks >= 41:
        grade = "D"
    else:
        grade = "F"
        
    return grade


# Call the calculate_average() function
avg = calculate_average(bengali_marks, english_marks, math_marks, science_marks)
# print(avg)

# Call the calculate_grade() function
result = calculate_grade(avg)
# print(result)

print("\n")  # For new line
# Print the grade report to the console.
print("---Report---")
print("Your obtained grade is:", result)
print("Your average number is:", avg)

