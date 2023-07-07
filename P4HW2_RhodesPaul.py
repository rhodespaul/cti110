# CTI-110

# P4HW2 - Salary Calculator

# Paul Rhodes

# 7/6/23

#Program to add employees to list, display pay/overtime pay and hours. and at end display total employees and total pay types

emp_name = input('Enter employee\'s name or \"Done\" to terminate: ')
terminate = "Done"
total_emp = []
total_ovrpay = []
total_regpay = []
total_grosspay = []


while emp_name != terminate:
    total_emp.append(emp_name)
    emp_hrs = float(input(f'How many hours did {emp_name} work? '))
    pay_rate = float(input(f'What is {emp_name}\'s pay rate? '))
    if emp_hrs > 40:
        ovr_hrs = emp_hrs - 40
        ovr_prate = (pay_rate / 2) + pay_rate
        ovr_pay = ovr_prate * ovr_hrs
        total_ovrpay.append(ovr_pay)
        reg_pay = pay_rate  * 40
        total_regpay.append(reg_pay)
        gross_pay = reg_pay + ovr_pay
        total_grosspay.append(gross_pay)
        print(f'Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay        Gross Pay')
        print(f'{emp_hrs:.1f}    {pay_rate:.2f}    {ovr_hrs:.1f}    {ovr_pay:.2f}    ${reg_pay:.2f}        ${gross_pay:.2f}')
        emp_name = input('Enter employee\'s name or \"Done\" to terminate: ')
    else:
        reg_pay = emp_hrs * pay_rate
        gross_pay = reg_pay
        total_regpay.append(gross_pay)
        total_grosspay.append(gross_pay)
        ovr_hrs = 0
        ovr_pay = 0
        print(f'Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay        Gross Pay')
        print(f'{emp_hrs:.1f}    {pay_rate:.2f}    {ovr_hrs:.1f}    {ovr_pay:.2f}    ${reg_pay:.2f}        ${gross_pay:.2f}')
        emp_name = input('Enter employee\'s name or \"Done\" to terminate: ')

else:
    print('Terminating program.')
    print()
    print(f'Total number of employees entered: {len(total_emp)}')
    print(f'Total amount paid for overtime: ${sum(total_ovrpay)}')
    print(f'Total amount paid for regular hours: ${sum(total_regpay)}')
    print(f'Total amount paid in gross: ${sum(total_grosspay)}')
