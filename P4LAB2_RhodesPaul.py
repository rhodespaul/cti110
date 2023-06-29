int_1 = int(input())
int_2 = int(input())

if int_2 >= int_1:
    for answer in range(int_1, int_2 + 1, 5, ):
        print(answer, end= ' ')
    print()
else:
    print('Second integer can\'t be less than the first.')


''' Type your code here. '''