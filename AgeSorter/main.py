#Sean Stack, ID:2511132 COP1000
#Chapter 7 Program
import random


def value_returning(age_nums):
  # newlist = [x for x in fruits if "a" in x]
  age_nums.sort(reverse=True)
  return age_nums


def main():
  # Generate 100 random integers, int_nums
  age_nums = [random.randint(1, 100) for x in range(1, 101)]
  result = value_returning(age_nums)
  total = 0
  # for loop in range 1 to 100 and hop by 20
  for index in range(0, 100, 20):
    # print(result[index], end=" ")
    for j in range(0, 20):
      if j != 19:
        print(f'{result[index + j]:<3d}', end=" ")
      else:
        print(f'{result[index + j]:<3d}')
  for value in age_nums:
    total += value
  print(' ')
  print(f'Sum of all ages: {total}')
  average = total / len(age_nums)
  oldest = max(age_nums)
  youngest = min(age_nums)
  print(f'Oldest age: {oldest}')
  print(f'Youngest age: {youngest}')
  print(f'Average age: {average:,.2f}')
  senior_count = 0
  minor_count = 0
  college_count = 0
  for j in range(0, 100):
    if age_nums[j] <= 18:
      minor_count += 1
    elif age_nums[j] >= 65:
      senior_count += 1
    elif age_nums[j] > 18 and age_nums[j] < 65:
      college_count += 1
  
  
  print(f'Number of minors: {minor_count}')
  print(f'Number of seniors: {senior_count}')
  print(f'Number of college aged: {college_count}')
  #built in function to determine the age of the oldest person
  #print the age of the oldest person

  #built in function to determine the age of the youngest person
  #print the age of the youngest person

  #determine the average age by making use of the sum of all ages calculated


main()
