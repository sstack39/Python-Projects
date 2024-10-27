#Sean Stack, ID: 2511132 COP1000
from temps import c_to_f, f_to_c


def main():
  # input the integer for temperature
  temp = int(input('Enter a temperature '))
  # input the unit for temperature
  unit = input('Was that input Fahrenheit or Celsius c/f? ')

  # use imported methods to convert entered temperature
  if unit == 'f':
    celsius = f_to_c(temp)
    print(float(celsius), 'Celsius equals', float(temp), 'Fahrenheit')
  elif unit == 'c':
    c_to_f(temp)
  # if unit if fahrenheit use f_to_c
  # else use c_to_f

if __name__ == '__main__':
  main()
