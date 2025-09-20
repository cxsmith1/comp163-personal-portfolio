from collections import namedtuple # type: ignore
import math

#Personal Information
full_name = "Caleb Smith"
email = "cxsmith1@aggies.ncat.edu"
hometown = "Durham, NC"
grad_semester = "Fall 2027"
major = "Information Technology"

#Academic Data Organization
current_courses = ["COMP 163", "MATH 104", "PHIL 104", "MGMT 221", "CHEM 100", "CHEM 110"]
completed_courses = ["CST 123", "MATH 103", "ECEN 100" ]
credit_hour_list = [3, 3, 3, 3, 3, 1]
gpa_history_list = [2.3, 2.54, 2.54]
cume_gpa = sum(gpa_history_list) / len(gpa_history_list)

#Contact Information Storage
Emergency_Contact = namedtuple("Emergency_Contact", ["Relation", "Name", "Phone_Number"] )
emergency_contact = Emergency_Contact("Mom","Hannah Smith", "704-555-0199")
Address = namedtuple("Address", ["Address", "City", "Zip_Code"])
addressfr = Address("456 Oak Street", "Durham, NC", "27707")
Instagram = namedtuple("Instagram", ["at","followers"])
instagramfr = Instagram("@mynamegohard", 517) 
Twitter = namedtuple("Twitter",["at","followers"])
twitterfr = Twitter("@cxs_72", 105)
followersum = instagramfr[1] + twitterfr[1]
Birthday = namedtuple("Birthday", ["Month", "Day", "Year"])
birthdayfr = Birthday("12","30", "2004")

#Interest Tracking
current_skills_set = {"Photography", "Problem solving", "C++ Basics", "Linux Basics", "System Administration Basics", "SQL Basics", "Python basics",}
skills_to_learn_set = {"Data structures", "Web design", "JavaScript", "Git", "Public speaking", "More SQL"}
career_interests_set = {'System Administration', 'Game development', 'Web development', 'Data science', "Cybersecurity"}
hobbies_set = ["Gaming", "Photography", "Reading", "Football", "Photoshop" "Video Editing"]
entertainment_backlog_set = ["Atlanta", "One Punch Man", "Life", "Wrestling", "NFL FIlms"]

#Organizational Mapping
course_credit_dictionary = {"COMP 163":  3, "MATH 104": 3, "MGMT 221": 3, "CHEM 100": 3, "PHIL 104": 3, "CHEM 110": 1}
coursesfr = sum(course_credit_dictionary.values())
course_professors_dictionary = {"COMP 163": "- Prof. Rhodes", "MATH 104": "- Prof. Williams", "PHIL 104": "- Dr. Foresman", "CHEM 100": "- Prof. Jackson"}
course_rooms_dictionary = {"COMP 163": '- M-Eric 300', "MATH 104": "- Marteena 212", "PHIL 104": "- Crosby 106", "CHEM 100": "- ACB 209"}
monthly_budget_dictionary = {"Food": 325, "Entertainment": 30, "Books": 10, "Transportation": 90}
Fewd = monthly_budget_dictionary["Food"]
Bewk = monthly_budget_dictionary["Books"]
tainment = monthly_budget_dictionary["Entertainment"]
twansport = monthly_budget_dictionary['Transportation']
budgetfr = sum(monthly_budget_dictionary.values())
study_hours_per_subject_dictionary = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
studyfr = sum(study_hours_per_subject_dictionary.values())
contact_directory_dictionary = {"Mom:": '704-555-0199', "Roommate:": 336-555-7821, "Academic Advisor:": 336-334-5000}

#Required Calculations


print('================================================================')
print('              PERSONAL ACADEMIC & LIFE PORTFOLIO')
print('================================================================')
print(f'Student: {full_name} | Email: {email}')
print(f'From: {hometown} | Graduating: {grad_semester}')
print(f'Major: {major}')
print('')

print('=== ACADEMIC PROFILE ===')
print(f'Current Semester:', sum(credit_hour_list), 'credits across', len(credit_hour_list), 'courses')
print(f'Cumulative GPA: {round(cume_gpa*100)/100}')
print(f'Weekly Study Time: {studyfr} hours')
print(f'Academic Investment: ${Bewk/studyfr:.1f} per study hour')
print('')
print(f'Current Courses:')
print(f'COMP 163 - {course_credit_dictionary['COMP 163']} credits {course_professors_dictionary['COMP 163']} {course_rooms_dictionary['COMP 163']}')
print(f'MATH 150 - {course_credit_dictionary['MATH 104']} credits {course_professors_dictionary['MATH 104']} {course_rooms_dictionary['MATH 104']}')
print(f'ENG 101 - {course_credit_dictionary['PHIL 104']} credits {course_professors_dictionary['PHIL 104']} {course_rooms_dictionary['PHIL 104']}')
print(f'HIS 105 - {course_credit_dictionary['CHEM 100']} credits {course_professors_dictionary['CHEM 100']} {course_rooms_dictionary['CHEM 100']}')

print('')

print("=== PERSONAL DEVELOPMENT ===")
print(f'Current Skills: {current_skills_set}')
print(f'Learning Goals: {skills_to_learn_set}')
print(f'Career Interests: {career_interests_set}')
print(f'Skills Currently Have: {len(current_skills_set)}')
print(f'Skills Want to Learn: {len(skills_to_learn_set)}')

print('')
print('=== FINANCIAL OVERVIEW ===')
print(f'Monthly Budget: ${budgetfr}')
print(f'Food: ${Fewd} (${Fewd/30:.1f}/day)')
print(f'Entertainment: ${tainment}')
print(f'Books: ${Bewk}')
print(f'Transportation: ${twansport}')
print(f'Annual Projection: ${budgetfr*12}')

print('')


print('=== CONNECTIONS & CONTACTS ===')
print(f'Emergency Contact: {emergency_contact.Name} ({emergency_contact.Relation}) - {emergency_contact.Phone_Number}')
print(f'Home Address: {addressfr.Address}, {addressfr.City} {addressfr.Zip_Code}')
print(f'Social Media Presence: {followersum} followers across 2 platforms')
print(f'Key Contacts: 3 people in directory')

print('')

print(f'=== LIFE STATISTICS ===')
print(f'Total Courses Completed: 5')
print(f'Current Academic Load: {studyfr + coursesfr} weekly commitments')
print(f'Entertainment Backlog: {len(entertainment_backlog_set)} items')
print(f'Current Hobbies: {len(hobbies_set)} activities')
print('================================================================')
