
miles_gallon = float(input())
cost_gallon = float(input())
cost_mile20 = (20 / miles_gallon) * cost_gallon
cost_mile75 = (75 / miles_gallon) * cost_gallon
cost_mile500 = (500 / miles_gallon) * cost_gallon
print(f'{cost_mile20:.2f} {cost_mile75:.2f} {cost_mile500:.2f}')




