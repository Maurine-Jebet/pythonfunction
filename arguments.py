def  year_of_birth(name,age):
    year = 2023-18
    print(f"Hello{name},you were born in {year}")

def my_country(country = "Kenya"):
    print(f"Hello you are from{country}")

def hello(*names) :
    for name in names:
        print(f"Hello {name}")   


def sum(*nums):
    answer = 0
    for num in nums:
        answer += num
    return answer
    

def multiply_many(**kwargs):
    answer = 1
    for num in kwargs.values():
        answer *= num
    return answer

# //Assignments 

def concatenate_args(*school):
    answer = ""
    for string in school:
        answer += string
    return answer    


def concatenate_kwargs(**kwargs):
    answer= ""
    for name in kwargs.values():
        answer+=name
    return answer
# positional arguments



def sum_multiplication(sum,multiplication):
    return(f"The sum of 2 and 6 is {sum} and the product is {multiplication}")
print(sum_multiplication(8,12))



# keywords arguments
# args
def firstname(*names):
    final = [name for name in names ]
    print(f"Hello {final}")

    for name in names:
        print(f"Hello {name}")
    
firstname("jebet",  "kitur",  "Morin")
# kwargs
def firstname(**kwargs):

    for name in kwargs.values():
        print(name)
        # return name
    
firstname(a ="morin",b = "jebet",c = "kitur")   
        
# //default arguments
def names(firstname = "Kitur",secondname = "jebet"):
    return(f'my name is {firstname} {secondname}')
print (names())
print (names(secondname="kitur",firstname="morin"))

name = "Maurine"
print(name[::-1])
print(name[1::-1])


    



