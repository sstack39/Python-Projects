#Sean Stack ID:2511132 COP1000


def print_formatted_string(first, second, third, fourth):
  print(f'{first:<20} {second:<20} {third:<20} {fourth:<10}')


count = 0
#create list for age entries to be stored
print_formatted_string('Book Title', 'Author Name', 'Discount ($)',
                       'Total Price after Discount ($)')
print(
    '-----------------------------------------------------------------------------------------'
)

with open('BookSale.txt', 'r') as f:
  #open friends.txt file
  book_title = None
  author = None
  reg_price = 0
  discount = 0
  new_discount = 0
  new_price = 0
  while f:
    entry = f.readline().strip()
    #read data from friends.txt file
    count += 1
    if count % 4 == 0:
      discount = entry
      new_discount = (float(reg_price) * (float(discount) / 100))
    elif count % 4 == 1:
      book_title = entry
    elif count % 4 == 2:
      author = entry
    else:
      reg_price = entry
      

#use counter to reorganize data from txt file, get the name and age
#add age entries to list
    if count % 4 == 0:
      #display in table
      new_price = float(reg_price) - float(new_discount)
      print(
          f'{book_title:<20} {author:<20} {float(new_discount):<20,.2f} {float(new_price):<10,.2f} '
      )
    if entry == "":
      break

#discount needs to be displayed as dollar amount out of regular price
#new total needs to be displayed as regular price - discount dollar amt
