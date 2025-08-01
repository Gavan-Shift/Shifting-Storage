'''원본 코드
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
'''

'''변경 1
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
'''

'''변경 2
x = input("What's x? ")
y = input("What's y? ")

print(int(x) + int(y))
'''

'''실패
print(int((input("What's x? ")) + input("What's y? ")))
'''

"""
print(int(input("What's x? ")) + int(input("What's y? ")))
"""