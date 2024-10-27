#Sean Stack, COP1000
#Chapter 4 Preparation Assignment 1

#Write a python program that uses a for loop with the range function to process
#the integers from 5 to 50 in increments of 5.


def print_formatted_string(first, second, third):
  print(f'{first:^7}\t{second:>8}\t{third:>12}')


def main():
  # print(' INTS\t SQUARES\t\t   CUBES')
  print_formatted_string('INTS', 'SQUARES', 'CUBES')
  for num in range(5, 51, 5):
    INTS = num
    SQUARES = num**2
    CUBES = num**3
    print(f'{INTS:^7,d}\t{SQUARES:>8,d}\t{CUBES:>12,d}')


main()
