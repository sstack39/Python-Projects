#Sean Stack, ID: 2511132 COP1000
#Dunders Test
import random


def show_larger():
  #generate two random int between 1 and 5.
  # Find a method to generate random integers
  first_num = random.randint(1, 5)
  second_num = random.randint(1, 5)

  #compare them and find the larger of the two.
  larger_num = first_num if first_num > second_num else second_num
  smaller_num = first_num if first_num <= second_num else second_num
  #get the difference
  difference = larger_num - smaller_num
  #print the message depending upon what the difference is.
  if difference != 0:
    print(larger_num, 'is larger than', smaller_num, 'by', difference)
  else:
    print('The integers are equal, both are ', smaller_num)


def main():
  show_larger()


if __name__ == '__main__':
  main()
