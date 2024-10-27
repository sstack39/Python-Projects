#Sean Stack, ID: 2511132 COP1000
#Chapter 9 Prep Program

def main():
  
  state_capitals = {"WA":"Seattle","TX":"Austin","CA":"Sacramento","FL":"Tallahassee"}
  print('4 states are in the dictionary')
  print("Let's add a few more ")
  while True:
    
    #input state abbreviations from user
    abbrev = input('Enter state abbrev. or Enter to quit ')
    #if abbreviation entered is blank, exit
    if abbrev == "":
      break
    #else "try" to append
    #if data is not there, it will be added to the dictionary
    if len(abbrev) > 2:
      continue
    #else output the capital
    if abbrev in state_capitals:
      print(f'Already have {abbrev}, capital is {state_capitals[abbrev]}')
    else:
      capital = input(f'Enter the capital of {abbrev} ')
      state_capitals[abbrev] = capital
  print(" ")
  print(f'Got {len(state_capitals)} states now. Here they are...')
  for key in state_capitals:
    print(f'The capital of {key} is {state_capitals[key]}')
  
  odd_int = { x:x ** 3 for x in range(1,10,2)}
  print()
  print('Some cubes made with a dictionary comprehension...')
  for key in odd_int:
    print(f'{key} cubed is {odd_int[key]}')

main()

