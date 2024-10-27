item_cost = float(input('Enter the cost in dollars: '))
change_due = 15 - item_cost
change_25 = change_due // 0.25
change25 = change_due % 0.25
change_10 = change_due // 0.10
change10 = change_due % 0.10
change_5 = change_due // 0.05
change5 = change_due % 0.05
change_1 = change_due // 0.01
change1 = change_due % 0.01

def main():
  print('Owed Amount Dispensed as Change: ')
  print('Quarters - ', (change_25))
  print('Dimes - ', (change_10))
  print('Nickels - ', (change_5))
  print('Pennies - ', (change_1))
main()