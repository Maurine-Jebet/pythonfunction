def even_numbers():
    x = range(10)
    for i in x:
        if i % 2 == 0:
            print(i)

def even_numbers():
    x = range(20)
    for i in x:
        if i % 2 != 0:
            print(i)

def divisible_by_five():
    x = range(50)
    for i in x:
        if i % 5 == 0:
            print(f"{i} is divisible by 5")
    else :
        print(f"{i}is not divisible by 5") 


def multiple_comparison():
    x = range(50)
    for i in x :
        if i % 5 == 0:
            print(f"{i}is divisible by 5") 
        elif i % 7 == 0:
            print(f"{i}is divisible by 7")           
        elif i % 9 == 0:
            print(f"{i}is divisible by 9" )
        else :
            print(f"{i} is not divisible by 5,7 or 9")  

def odd_or_even():
    x = range (20)
    for i in x:
        if i % 2==0 and i % 3 == 0:
            print(f"{i} is divisible by both 2 and 3")

        elif i % 2 == 0  or i %3 == 0:
            print(f"{i}is divisible by either 2 or 3")
        else:
            print(f"{i}is not divisible by either 2 or 3")  

def while_loop():
    x = 1
    while x < 10 :
        print("Hello")
        x+=1



def break_statement():
    x = 1
    while x < 10:
        print("Hello")
        x+=1
        if x == 5:
            break     


def continue_statement():
    x = 0
    while x <=20:
        x+=1
        if x %3 ==0:
            continue
        print(x)
    
# //Write a function that uses while, if and continue statements to print
# //all the even numbers between 0 and 50. 


def continue_statements():
    x = 0
    while x <50:
        x+=1
        if x %2 !=0:
            continue
        print(x)





# Write a function that takes an integer argument and prints "Prime" if the 
# number is prime, and "Not prime" if the number is not prime.
def int_argument(x):
    y= range(2, x)
    for i in y:
        if i % x ==0:
            print(f"{i}prime")

        else: 
            i % x != 0
            print(f"{i}Not prime")

            
       




# Write a function that takes a list of integers as input and prints the 
# sum of all the even numbers in the list.

def integers():
    x = range(20,30)
    sum = 0
    for i in x:
        if i % 2 == 0:
            print(sum)
            sum = sum + i
        else:
            print("not") 
    print(sum)           







# Write a function that takes any two integers as input, and prints the sum
# # of all the numbers between the two integers (inclusive) that are divisible by 3.dedef sum_between(first, second):
# def nums_between():
#     x = range(10,15)
#     sum = 0
#     for i in x:
#         if i % 3 == 0:
#             print(sum)
#         else:
#             print("not divisible")
#             sum = sum + i
#             print(sum)    


def sum_numbers_between(first,second):
    sum_between=0
    for num in range(first,second+1):
        sum_between=sum_between+num
        if num % 3==0:
            print(sum_between)


























    



