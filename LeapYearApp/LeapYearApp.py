'''
#write program leap year or not
#input(num), code(if %), output(print odd or even), 
#Prompt user to enter a number
year = int(input('Enter year to determine if leap year '))
#Calculate if num is odd or even
#divible by 4 and not century year(not divisible by 100) 1800 1996
#divisible by 400 for century year 2000,
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, 'is a leap year')
else:
  print(year, 'is not a leap year')

#write program to check value of username and password
#input(username and password from user), code(compare strings ==), output(please try again username is incorrect, please try again password is incorrect, Welcome!)
#Prompt the user for username
#Prompt the user for password
username = input('Enter Username ')
password = input('Enter Password ')
if username == 'sstack':
  if password == 'hello123':
    print('Welcome Sean!')
  else:
    print('Your password is incorrect, please try again')
else:
  print('Your username is incorrect, please try again')
    

#write a program
#get student name
#get 6 subjects grades -> pass(60 and above) or fail(below 60)
#if pass cal average -> grade wrt average D(60 to 69) C(70 to 79) or B(80 TO 89) and A(90 TO 100) 
name = input('What is your name? ')
subject1 = int(input('Enter number grade '))
subject2 = int(input('Enter number grade '))
subject3 = int(input('Enter number grade '))
subject4 = int(input('Enter number grade '))
subject5 = int(input('Enter number grade '))
subject6 = int(input('Enter number grade '))
  
if subject1 <60 or subject2 <60 or subject3 <60 or subject4 <60 or subject5 <60 or subject6 <60:
  print('Fail')
else:
  total = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
  average = total / 6
  print(f'{average:,.2f}', 'Pass')
  #60 to 69
  if average > 60 and average < 69:
    print('Congratulations', name, 'You got a D!')
  elif average > 70 and average < 79:
    print('Congratulations', name, 'You got a C!')
  elif average > 80 and average < 89:
    print('Congratulations', name, 'You got a B!')
  else:
    print('Congratulations', name, ', You got a A!')
    

#Homework Counting coin Problem
insert $10 (input)
amount to be paid is $8.87 (input)
remain $1.13 -> 113 cents
4 quaters, 
remain 13 cents (13/10)
1 dime
remain 3 cents
0 nickel
3 penny
'''

item_cost = float(input('Enter the cost in dollars: '))
change_due = 10 - item_cost #1.13
change_25 = change_due // 0.25 # 4
change25 = change_due % 0.25 
#print(change25) #0.13
change_10 = change25 // 0.10 #
change10 = change25 % 0.10
#print(change10) #0.13
change_5 = change10 // 0.05
change5 = change10 % 0.05
change_1 = change5 // 0.01
change1 = change5 % 0.01

def main():
  print('Owed Amount Dispensed as Change: ')
  print('Quarters - ', int(change_25))
  print('Dimes - ', int(change_10))
  print('Nickels - ', int(change_5))
  print('Pennies - ', int(change_1))
main()















