#Sean Stack, ID: 2511132 COP1000


def main():
  # list of number from 0 to 9
  numbers = "09876543210"
  # for loop to loop 3 times
  for i in range(0, 3):
    for num in range(0, len(numbers)):
      print(numbers[:num:-1])
  # print the numbers in the list for each loop

main()

