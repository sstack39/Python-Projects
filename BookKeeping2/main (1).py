#Sean Stack, ID:2511132 COP1000

#create BookSale.txt file
list_entries = []
with open('BookSale.txt', 'w') as f:
  while True:
    book_title = input('Enter the book title: ')
    # Use the infinite while loop
    if book_title == "":
      break
# Prompt the user Book title, author's name, price, and discount
# Check for Enter to exit the while loop
    author = input("Enter the author's name:  ")
    reg_price = input('Enter the regular price: ')
    discount = input('Enter the discount in percent: ')
    list_entries.append(book_title + '\n')
    list_entries.append(author + '\n')
    list_entries.append(reg_price + '\n')
    list_entries.append(discount + '\n')
    
# write the line to file
  f.writelines(list_entries)

print('The book sale data has been successfully stored in BookSale.txt.')

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