#Sean Stack ID:2511132, COP1000
from function_5_1 import subtotal

#prompt user to enter number of books being purchased
quantity = int(input('Enter the number of books being purchased: '))

all_subtotals = []
#Use loop in main function the number of times user enters number of books.
for book_no in range(1, quantity + 1):
  print(f'\nBook {book_no}: ')
  # Prompt user for title of the book
  title = input('Enter the book title: ')
  # Prompt user ISBN no.
  input('Enter the ISBN number: ')
  # Prompt user for Price
  price = float(input('Enter the price: '))
  # Prompt user for quantity
  book_quantity = int(input('Enter the quantity: '))
  # call the imported method and receive the subtotal
  sub_total = subtotal(price, book_quantity, title)
  # add this book's sub_total to all_subtotals
  all_subtotals.append(sub_total)

total = 0
# for loop over all_subtotals
for sub_total in all_subtotals:
  # add the value to sum_of_subtotals
  total += sub_total
print(f'\nTotal: ${total}')
# print the total
