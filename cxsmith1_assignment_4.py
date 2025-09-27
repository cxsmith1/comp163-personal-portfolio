from collections import namedtuple
import math


#Student stat intake (prompts user for Name, GPA, Study Time, and Stress levels)
student_name = input('Please enter your name:')
current_gpa = float(input('Enter your current GPA:'))
study_hours = int(input('Enter how many hours you study per week:'))
social_points = int(input('How would you rate your social life on a scale of 1-100?:'))
stress_level = int(input("Rate your stress level 1-100:"))

#Student stat display (displays Name, GPA, Study Time, and Stress levels)
print('Welcome to the show! Here are your starting stats:')
print(f'Name        | {student_name}')
print(f'Current GPA | {current_gpa}')
print(f'Study Hours | {study_hours}')
print(f'Social Pts  | {social_points}')
print(f'Stress Lvl  | {stress_level}')



    
    
    
    
