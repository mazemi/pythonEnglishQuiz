# Developed by Mohammad Azemi.
# My target is to practice reading an MS Excel file and using external libraries.

from typing import List, Any
import pandas as pd
import random

print('WELCOME TO ENGLISH TEST!')
print('For exit the app enter "q"')
print('Please enter "t" for True and "f" for False')
print('')

random_questions = random.sample(range(1, 830), 10)
random_dari = random.sample(range(1, 550), 10)

try:
    true_data = pd.read_excel(r'engDari.xls', sheet_name=0)
    df1 = pd.DataFrame(true_data)
    true_list = df1.values.tolist()

    false_data = pd.read_excel(r'engDari.xls', sheet_name=1)
    df2 = pd.DataFrame(false_data)
    false_list = df2.values.tolist()

except:
    print("there is an error in reading excel file!")
    raise SystemExit

score = 0
one_two_list = []
complete_list = []
right_response_list: list[Any] = []


for question in range(10):
    one_or_two = random.randint(1, 2)
    # one_two_list.append(one_or_two)
    complete_list = true_list[random_questions[question]]
    # print(complete_list)
    complete_list.append(false_list[random_dari[question]][0])
    complete_list.append(one_or_two)
    # print(complete_list)
    if complete_list[3] == 1:
        print(str(question + 1) + "): " + complete_list[0] + " : " + complete_list[1], end=' ')
    else:
        print(str(question + 1) + "): " + complete_list[0] + " : " + complete_list[2], end=' ')

    while True:
        # user_response = input("true or false?")
        user_response = input("")
        if user_response.upper() not in ('T', 'F', 'Q'):
            print("Please enter t for true or f for false.")
        else:
            break

    if user_response.upper() == "Q":
        raise SystemExit

    if (user_response.upper() == "T" and one_or_two == 1) or (user_response.upper() == "F" and one_or_two == 2):
        # print("right")
        score = score + 1
    elif (user_response.upper() == "T" and one_or_two == 2) or (user_response.upper() == "F" and one_or_two == 1):
        # print("wrong")
        right_response_list.append(complete_list[0] + " : " + complete_list[1])
print('')

if score == 10:
    print('*********************************')
    print(u"\u2713" + " Awesome! your score is " + str(score) + " of 10")
    print('*********************************')
else:
    print('---------------------')
    print("your score is " + str(score) + " of 10 ")
    print('---------------------')
    print('The right meaning of your wrong responses:')
    for z in range(len(right_response_list)):
        print(right_response_list[z])