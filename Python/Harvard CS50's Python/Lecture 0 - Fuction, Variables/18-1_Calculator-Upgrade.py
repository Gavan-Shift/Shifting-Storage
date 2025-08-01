print("Welcome to the Calculator Upgrade!")
print("First Step!")                                                            # 정수형, 실수형 구분 입력
print("Please enter the form of the number you want to calculate")
print("If you want enter Integers, you can enter \"I\"")                        # 정수형 입력 : I
print("If you want enter Floats, you can enter \"F\"")                          # 실수형 입력 : F
number_type = input("Number Type : ")
print("# "*100)

print("Second Step!")                                                           # 계산할 숫자 입력
print("Please enter the numbers you want to calculate")

# 숫자 타입에 따라 적절한 변환 함수 사용
if number_type == "I":
    X = int(input("X : "))
    Y = int(input("Y : "))
elif number_type == "F":
    X = float(input("X : "))
    Y = float(input("Y : "))
else:
    print("Invalid number type! Please enter 'I' or 'F'")
    exit()

print("# "*100)
print("Last Step!")                                                              # 연산자 입력
print("Please enter the type of operator you want to calculate")
print("If you want to add, you can enter \"+\"")                                 # 더하기 : +
print("If you want to subtract, you can enter \"-\"")                            # 빼기 : -
print("If you want to multiply, you can enter \"*\"")                            # 곱하기 : *
print("If you want to divide, you can enter \"/\"")                              # 나누기 : /
print("If you want to divide and get the integer part, you can enter \"//\"")    # 몫 : //
print("If you want to get the remainder, you can enter \"%\"")                   # 나머지 : %
print("If you want to raise to the power, you can enter \"**\"")                 # 거듭제곱 : **
operator = input("Operator : ")
print("# "*100)

print("Calculating the result...")

# 계산 수행
if operator == "+":
    result = X + Y
elif operator == "-":
    result = X - Y
elif operator == "*":
    result = X * Y
elif operator == "/":
    if Y == 0:
        result = "Error: Division by zero"
    else:
        result = X / Y
elif operator == "//":
    if Y == 0:
        result = "Error: Division by zero"
    else:
        result = X // Y
elif operator == "%":
    if Y == 0:
        result = "Error: Division by zero"
    else:
        result = X % Y
elif operator == "**":
    result = X ** Y
else:
    result = "Invalid Operator"

print("# "*100)

# 결과 출력
if isinstance(result, str):                                                        # 오류 메시지인 경우
    print(result)
else:
    print(f"The result of {X} {operator} {Y} is: {result}")