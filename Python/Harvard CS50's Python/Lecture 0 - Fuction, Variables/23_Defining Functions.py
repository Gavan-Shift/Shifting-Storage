""" 23_Defining Functions.py """
#######################################################################
'''1
# Ask user for their name
name = input("What's your name? ").strip().title()

# Say hello to user
print(f"hello, {name}")
'''
#######################################################################
""" 이런 식으로 사용하고 싶다"""
'''2
name = input("What's your name? ")
hello()
print(name)
'''
#######################################################################
'''3
def hello():                            # [의미] 이 코드 줄 아래의 들여쓰기한 모든 코드를 이 함수의 의미로 취급
    print("hello, ")

name = input("What's your name? ")
hello()
print(name)
'''
#######################################################################
'''4
def hello():                            # [의미] 이 코드 줄 아래의 들여쓰기한 모든 코드를 이 함수의 의미로 취급
    print("hello, ", end="")            # [의미] 이 함수가 호출되면 "hello, "를 출력, 줄 바꿈 X

name = input("What's your name? ")
hello()
print(name)
'''
#######################################################################
'''5
def hello(to):                            # [의미] 이 코드 줄 아래의 들여쓰기한 모든 코드를 이 함수의 의미로 취급
    print("hello, ", to)                  # [의미] 이 함수가 호출되면 "hello, "를 출력, 줄 바꿈 X

name = input("What's your name? ")
hello(name)                               # [의미] hello() 함수에 name 변수를 인자로 전달
'''
#######################################################################
'''
def hello(to="world"):                            # [의미] 이 코드 줄 아래의 들여쓰기한 모든 코드를 이 함수의 의미로 취급
    print("hello, ", to)                  # [의미] 이 함수가 호출되면 "hello, "를 출력, 줄 바꿈 X

hello()
name = input("What's your name? ")
hello(name)                               # [의미] hello() 함수에 name 변수를 인자로 전달
'''
#######################################################################