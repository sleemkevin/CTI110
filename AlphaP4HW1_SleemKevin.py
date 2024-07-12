#Kevin Sleem
#July 10, 2024
#P4HW1
#Grade Calculator

#Enter grades
num_scores =int(input('How many scores do you want to enter? '))
scorelist = []
for i in range(1, num_scores+1):
    score = float(input(f'Enter score #{i}: '))
    scorelist.append(score)
    if score < 0 or score > 100:
        print('INVALID score entered!!!!')
        score = float(input(f'Enter score #{i} again: '))

#Skip a line
print('\n')
print('------------Results------------')
#Create list storing grades from module 1 through 6
#print lowest grade using list function min
print(f'{"Lowest Grade:":<20} {min(scorelist)}')
#print highest grade using list function max
print(f'{"Highest Grade:":<20} {max(scorelist)}')
#print sum of grades using list function sum
print(f'{"Sum of Grades:":<20} {sum(scorelist)}')
#create assignment for average of grades
average = sum(scorelist) / len(scorelist)
#print average
print(f'{"Average:":<20} {average:.2f}')
print('--------------------------------------')
