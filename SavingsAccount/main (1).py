#Sean Stack, ID:2511132, COP1000

#DEFINE variables necessary for program operation.
#PROMPT user to enter their savings goal for the week.

def main():
  # user enters their goal
  goal = int(input('Enter your savings goal for the week: '))

  # While loop
  days_count = 0
  total_savings = 0
  while True:
    saved = int(input('Enter the amount saved today (enter 0 to finish): '))
    if saved == 0:
      break
    # add saved to savings
    days_count += 1
    total_savings += saved
  # Users enters their saving for the day
  # exit while loop on 0
  # print the number days user saved
  # length of savings
  print(f"You have saved for {days_count} days.")
  # print how much user saved
  print(f'You have saved a total of ${total_savings}.')
  # print their saving in comparison to their goal.
  if total_savings < goal:
    print(f'Unforntunately, you did not meet your savings goal. You are ${goal - total_savings} under your goal. Try to save more next week!')
  else:
    print('Congratulations, you have met your savings goal!')

main()
