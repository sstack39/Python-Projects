#How many pounds are you ordering? 15
#Cost of coffee $150.00
#7% sales tax $10.50
#Shipping fee $15.00
#Total payable $175.50

#SAMPLE OUTPUT
#How many pounds are you ordering? 50
#Cost of coffee $375.00
#7% sales tax $26.25
#Shipping fee $0.00
#Total payable $401.25

forty = float(7.50)
twenty = float(8.75)
ten = float(10.00)
one_to_nine = float(12.00)
order_amt = float(input('How many pounds are you ordering? '))


subtotal = order_amt * float({forty,twenty,ten,one_to_nine})
def main():
    print('MoonBucks Coffee Company - Coffee Prices')
    print('40 pounds or more '      '  $7.50 per lb.')
    print('20 pounds or more '      '  $8.75 per lb.')
    print('10 pounds or more '      '  $10.00 per lb.')
    print('1 to 9 pounds     '      '  $12.00 per lb.')
    print('')
    print('')
    order_amt = float(input('How many pounds are you ordering? '))
    subtotal = 0.0
    if order_amt >= 40:
      subtotal = order_amt * forty
    elif order_amt >= 20:
      subtotal = order_amt * twenty
    elif order_amt >= 10:
      subtotal = order_amt * ten
    elif order_amt >= 1 <= 9:
      subtotal = order_amt * one_to_nine
    print(f'Cost of coffee ${subtotal:,.2f}')
    sales_tax = order_amt_base_cost * float(.07)
    no_shipping_fee =float(0.00)
    shipping_fee = subtotal * float(1.00)
    total_payable = subtotal + shipping_fee + sales_tax
    if subtotal <= 150:
         shipping_fee == subtotal
    elif subtotal >= 150:
        shipping_fee == no_shipping_fee
    print(f'7% sales tax ${sales_tax: ,.2f}')
    print(f'Shipping fee ${shipping_fee:,.2f}')
    print(f'Total payable ${total_payable:,.2f}')
main()
