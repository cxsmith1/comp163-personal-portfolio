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

print('')

# Course planning decision
print("Choose your course load:")
study_list = ['Easy', 'Medium', 'Hard']
print("Easy   | 12 Credits")
print("Medium | 15 Credits")
print("Hard   | 18 Credits")

print('')

decision = input("Your choice: ")

print('')

# Validate input and process choices
if decision not in study_list:
    print("Invalid choice. Please restart and select Easy, Medium, or Hard.")

elif decision == "Easy":   # Easiest Choice
    if current_gpa >= 3.0:
        print("You should do very well on easy mode.")
        study_hours += 5
        stress_level += 5
    else:
        print("Easy mode might be better for bringing up your GPA.")
        study_hours += 8
        stress_level += 3

elif decision == "Medium":  # Standard load
    if current_gpa >= 3.0:
        print("Medium difficulty should be manageable for you. Stay locked in!")
        study_hours += 10
        stress_level += 10
    else:
        print("Medium difficulty could be challenging with your GPA. Lock in twin.")
        study_hours += 15
        stress_level += 15

elif decision == "Hard":  # Heavy load
    if current_gpa >= 3.5:
        print("Taking on Hardcore Mode! LOCK IN TWIN!")
        study_hours += 20
        stress_level += 20
    else:
        print("Hardcore Mode... are you sure? I would advise to not do that.")
        study_hours += 25
        stress_level += 30

# Print updated stats
print("\nUpdated stats after your decision:")
print(f"Study Hours | {study_hours}")
print(f"Stress Lvl  | {stress_level}")


