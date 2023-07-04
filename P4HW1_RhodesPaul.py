# CTI-110

# P4HW1 - Score List

# Paul Rhodes

# 7/4/23

#User inputed scores, stored in list then displayed min, modified list with dropped lowest score and average with letter grade

score_list = []
score_total = 0
num_scores = int(input('How many scores would you like to enter? '))
print()

#For/loop/if of scores stored in list

for s in range(num_scores):
    score = float(input(f'Enter Score #{s+1}: '))
    if score >= 0 and score <= 100:
        score_list.append(score)
        score_total += score
    elif  score >= 101 or score < 0:
        score = float(input(f'Invalid score entered! Score should be between 0 and 100. Enter Score #{s+1}: '))
        score_list.append(score)
        score_total += score

        while score >= 101 or score < 0:
            score = float(input(f'Invalid score entered! Score should be between 0 and 100. Enter Score #{s+1}: '))
            
print()

score_average = score_total / num_scores

# Displayed Results

print('Results')
print(f'Lowest Score: {min(score_list)}')

#Remove Lowest Score
score_list.remove(min(score_list))

print(f'Modified List: {score_list}')
print(f'Scores Average: {score_average:.2f}')

#Letter grade for Average

if score_average >= 90:
    print('Your grade is: A')
elif score_average >= 80:
    print('Your grade is: B')
elif score_average >= 70:
    print('Your grade is: C')
else:
    score_average >= 60
    print('Your grade is: F')
            
