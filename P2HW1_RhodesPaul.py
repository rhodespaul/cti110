# A program to calculate the remaining funds left after expenses on a travel/trip.

# 6/8/23

# CTI-110 P1HW2 - Travel Expense

# Paul Rhodes

#This programe calculated the amount of remaining money that is left after expenses on a travel, it starts with starting budget then subtracts the amount for each expense then displays output to the user

print('This program calculates and displays travel expenses.')
user_budget = float(input('Enter Budget: '))
print()
user_dest = (input('Enter your travel destination: '))
print()
user_gas = float(input('How much will you spend on gas? '))
print()
user_liv = float(input('Approximately, how much will you need for accomodation/hotel? '))
print()
user_food = float(input('Last, how much do you need for food? '))
print('------------Travel Expenses------------')
print(f'Location:             {user_dest}')
print(f'Initial Budget:       ${user_budget:.1f}')

print(f'Fuel:                 ${user_gas:.1f}')
print(f'Accomodation:         ${user_liv:.1f}')
print(f'Food:                 ${user_food:.1f}')
print('---------------------------------------')

user_exp = user_gas+user_liv+user_food
user_bal = user_budget-user_exp
print(f'Remaining Balance:    ${user_bal}')






