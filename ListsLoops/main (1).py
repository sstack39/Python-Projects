#Sean Stack, ID:2511132 COP1000
#Chapter 7 Prep Program
import random

def change_list(int_list):
  # slice and get middle 6 elements of int_list
  # indexes = slice(4, 10)
  # new_list = int_list[indexes]
  new_list = int_list[4:10]
  # use a function to print the size of the new list
  print(f'The size of the list is now {len(new_list)}')
  # return the new list in ascending order
  new_list.sort()
  return new_list

  
def main():
  
  # Part 1.
  # Define a list
  int_list = []

  # Run a for loop 12 times
  for num in range(0, 12):
    int_list.append(random.randint(50, 101))
  # add a random integer between 50 to 100 to the list
  # Part 2.
  print()
  print('Here is the list of random integers...')
  print()
  for num in int_list:
    if num != int_list[11]:
      print(num, end=" ")
    else:
      print(num)
  # loop over the list that we just created
  # print the element *separated by comma*
  # Part 3.
  print()
  print(f'The 4th element in the list is {int_list[3]}')
  # Display the fourth element
  # Display the element at 9th index
  print(f'The element at index 9 is {int_list[9]}')
  # Display the smallest element
  print(f'The smallest element in the list is {min(int_list)}')
  
  # Part 4.
  # uncomment the below line
  new_list = change_list(int_list)
  # loop over the new_list
  print()
  for num in new_list:
    if num != new_list[5]:
      print(num, end=" ")
    else:
      print(num)
  # print numbers seperated by space
main()
