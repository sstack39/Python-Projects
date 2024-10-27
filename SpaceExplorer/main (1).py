#Sean Stack, ID:2511132 COP1000



def main():
  
  for num in range(1000,1101):
    text = None
    if num % 7 == 0 and num % 5 == 0:
      text = 'Star Explorer!'
    elif num % 5 == 0:
      text = 'Galaxy'
    elif num % 7 == 0:
      text = 'Universe'
    else:
      continue
    print(f'{num:^4}\t{text:<13}')

main()