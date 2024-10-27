def f_to_c(temp):
  # convert fahrenheit to celsius °C = (°F - 32) × 5/9
  # return celcius temperature
  celsius = (temp - 32) * (5/9)
  return celsius
  

def c_to_f(temp):
  #convert celsius to fahrenheit (0°C × 9/5) + 32 = 32°F

  fahrenheit = (temp * (9/5)) + 32
  #print celsius temperature
  print(float(fahrenheit),'Fahrenheit equals',float(temp),'Celsius')