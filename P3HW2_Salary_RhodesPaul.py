# CTI-110

# P3HW2 - Salary

# Paul Rhodes

# 6/26/23

#A program that displays the emp name, hours, pay, and any overtime hours and pay

emp_name = input('Enter employee\'s name: ')
hrs_wrk = float(input('Enter number of hours worked: '))
emp_pay = float(input('Enter employees\'s pay rate: '))

print('-------------------------------------')
print(f'Emplyee name:  {emp_name}')

ovr_hrs = hrs_wrk - 40
ovr_pay = (emp_pay / 2) + emp_pay
ovr_prate = ovr_pay * ovr_hrs
reg_pay = emp_pay * 40
grs_pay = ovr_prate + reg_pay

print()
print(f'Hours Worked    Pay Rate    OverTime    OverTime Pay        RegHour Pay        Gross Pay')
print('---------------------------------------------------------------------------------------------------')
print(f'{hrs_wrk}       {emp_pay}   {ovr_hrs}   {ovr_prate:.2f}     ${reg_pay:.2f}     ${grs_pay:.2f}')
