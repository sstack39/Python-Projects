#Sean Stack, COP1000
#Chapter 4 Preparation Assignment 2


#Write a python program that prompts the user to enter an integer and reports
#whether the input was even or odd.

#Assume that the user follows instructions and enters only integers.
#Must use a while loop and it should continue until the user enters 0.




def main():
#SET while loop as true statement to begin testing user input.    
    while True:
#PROMPT user to enter an integer or 0 to quit by defining int input as variable.       
        num = int(input('Enter an integer or 0 to quit '))        
#DEFINE sentinel as parameter that tests whether integer number is equal
#to 0. If true, break the loop.
        if num == 0:
            print('All done!')
            break
#DEFINE an accepted integer number as a new variable that can now test for remainder value
#in order to determine odd or even status.
        true_num = num % 2
#USE if/else statement to test and display whether or not the integer input is odd or even.
        if true_num > 0:
            print(num,'is an odd number')
        else:
            print(num,'is an even number')
#COMPLETE main statement block with main().        
main()
