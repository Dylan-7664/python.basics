#if statements
#store data list, tuple, dictionary
#loops
entered_value = input('Enter The Score:')
#print(type(entered_value))
#print(type(71))
#print(type(55.22))
if not entered_value.isnumeric():
    print('Please enter a valid number')
    exit(0)

score= int(entered_value) #convert to a number--integer
if score>= 78:
    print('A')
elif score>= 71 and score<=77:
    print('A-')
elif score >= 64 and score <= 70:
    print('B+')
elif score >= 57 and score <= 63:
    print('B')
elif score >= 50 and score <= 56:
    print('B-')
elif score >= 43 and score <= 49:
    print('C+')
else:
    print('D')
