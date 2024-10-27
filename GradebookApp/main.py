#Sean Stack, ID:2511132 COP1000
#Chapter 9_1 Program

import random
gradebook = {}
slice = {}

def custom_function(gradebook):
  print()
  print(f'{"Course":<8} {"Avg":^5} {"Grades":>25}')
  
  
  term_avg_full = list()
  
  for key in gradebook:
      average = sum(gradebook[key])/len(gradebook[key])
      term_avg_full.append(average)
      print(f'{key:<8} {average:^5,.1f}',end='')
      for grade in gradebook[key]:
        print(f'{grade/100:>6,.0%}',end='')
      print()
  print(f'Term Average: {sum(term_avg_full)/len(term_avg_full)/100:.1%}')
  print()
  print('Dropping the lowest grade from each course.')
  print()
  print(f'{"Course":<8} {"Avg":^5} {"Grades":>25}')
  term_avg_dropped = []
  for key in gradebook:
      #term_avg_full.append(average)
      lowest = min(gradebook[key])
      gradebook[key].remove(lowest)
      average = sum(gradebook[key])/len(gradebook[key])
      term_avg_dropped.append(average)
      print(f'{key:<8} {average:^5,.1f}',end='')
      for grade in gradebook[key]:
        print(f'{grade/100:>6,.0%}',end='')
      print()
  print(f'Term Average: {sum(term_avg_dropped)/len(term_avg_dropped)/100:.1%}')
  #print()
  #print(f'Dropping course {dropped_course} with the lowest average.')
  print() 
  lowest_course_avg = min(term_avg_dropped)
  
  #search for the course gradebook[key], to determine course with avg = lowest avg
  #for loop for key in gradebook
  drop_course_name = None
  for key in gradebook:
    average = sum(gradebook[key])/len(gradebook[key])
  #sum of gradebook[key]/len of gradebook[key] = avg
    if average == lowest_course_avg:
       drop_course_name = key

  print(f'Dropping course {drop_course_name} with lowest average.')
  print()
  print(f'{"Course":<8} {"Avg":^5} {"Grades":>25}')
  #if avg = lowest avg
  #key = name of lowest avg course
  term_avg_dropped.remove(lowest_course_avg)
  for key in gradebook:
    average = sum(gradebook[key])/len(gradebook[key])
    if average == lowest_course_avg:
       continue
    print(f'{key:<8} {average:^5,.1f}',end='')
    for grade in gradebook[key]:
        print(f'{grade/100:>6,.0%}',end='')
    print()
   
  
  print(f'Term Average: {sum(term_avg_dropped)/len(term_avg_dropped)/100:.1%}')
while True:
  #ask course code from user
  course_code = input('Enter course code or press enter to finish: ')
  
  #if course code is empty, exit while loop
  if course_code == "":
    break
  #assign course code as key
  value = [random.randint(60,100) for x in range(0,5)]
  value.sort()
  gradebook[course_code] = value
  #generate a list of 5 random integers between 60 and 100
  #assign that list as the value to the key
#call custom function with gradebook 
custom_function(gradebook)
