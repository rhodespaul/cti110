num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

int_product = int(round(num1 * num2 * num3 * num4))
int_average = int(num1 + num2 + num3 + num4) / 4
float_product = float(num1 * num2 * num3 * num4)
float_average = float(num1 + num2 + num3 + num4) / 4
print(f'{int_product:.0f} {int_average:.0f}')
print(f'{float_product:.3f} {float_average:.3f}')