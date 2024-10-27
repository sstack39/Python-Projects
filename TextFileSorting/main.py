#Sean Stack, ID: 2511132 COP1000
#Chapter 6 Prep Program 2

age_list = []
count = 0
#create list for age entries to be stored
with open('friends.txt', 'r') as f:
  #open friends.txt file
  age = None
  name = None
  while f:
    entry = f.readline().strip()
    #read data from friends.txt file
    count += 1
    if count % 2 == 0:
      age = entry
      age_list.append(int(age))
    else:
      name = entry
#use counter to reorganize data from txt file, get the name and age
#add age entries to list
#display data from text file as "My friend __ is __"
    if count % 2 == 0:
      print(f'My friend {name} is {age}')
    if entry == "":
      break
#find the average age and display

avg = sum(age_list)/len(age_list)
print(f'Average age of friends is {avg:.1f}')
