# CTI-110

# P2HW2 - List

# Paul Rhodes

# 6/16/2023

# A program that logs the grades for each module, inputed by the user, then lists the user inputs and averages the total, to be displayed



module_grade1 = float(input('Enter grade for Module 1: '))
module_grade2 = float(input('Enter grade for Module 2: '))
module_grade3 = float(input('Enter grade for Module 3: '))
module_grade4 = float(input('Enter grade for Module 4: '))
module_grade5 = float(input('Enter grade for Module 5: '))
module_grade6 = float(input('Enter grade for Module 6: '))

grades = [module_grade1, module_grade2, module_grade3, module_grade4, module_grade5, module_grade6]
grades_avg = (module_grade1 + module_grade2) / 2
grades_sum = module_grade1 + module_grade2 + module_grade3 + module_grade4 + module_grade5 + module_grade6
print()
print('------------Results------------')
print(f'Lowest Grade:       {min(grades)}')
print(f'Highest Grade:      {max(grades)}')
print(f'Sum of Grades:      {grades_sum:.1f}')
print(f'Average:            {grades_avg:.2f}')
print('----------------------------------------')

