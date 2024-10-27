#PROMPT user to enter their age.
#DEFINE all variables needed to complete program.

BASE_COST = 200
YOUNG_FEE = 50
SESSION_1 = 40
SESSION_2 = 70
SESSION_3 = 100
YOUNG_AGE = 25
MIN_AGE = 18
#DEFINE main statement block.
def main():
  AGE = int(input('Enter your age: '))
  BASE_FEE = BASE_COST
  YOUNG_FEE = 0
  if AGE < MIN_AGE:
    print('Membership Denied')
  else:
    SESSION = int(input('Enter the number of personal training sessions attended: '))
  if AGE < YOUNG_AGE:
    BASE_FEE = YOUNG_FEE + BASE_COST
  elif AGE > YOUNG_AGE:
    YOUNG_FEE = 0
  if SESSION == 1:
    SESSION = SESSION_1
  elif SESSION == 2:
    SESSION = SESSION_2
  elif SESSION >= 3:
    SESSION = SESSION_3
#USE if-elif statements to determine correct costs associated with user input.

#CALCULATE total amount owed to gym.
  total_cost = BASE_FEE + SESSION + YOUNG_FEE
#DISPLAY all of the correct information according to instructions.
  print('Your base membership fee is: $200.00')
  print(f'Your young member fee is : ${YOUNG_FEE:,.2f}')
  print(f'Your personal training sessions cost is: ${SESSION:,.2f}')
  print(f'Your total membership cost is: ${total_cost:,.2f}')
  
main()
        


        
