# split : 문자열을 여러 개의 하위 문자열로 분할하는 함수
# ex) 사용자가 입력한 이름을 이름과 성으로 분리할 수 있다.
# name.split(" ") : 공백을 기준으로 문자열을 분리
# first_name, last_name = name.split(" ")

# [Code Example] #

#######################################################################

# Ask user for their name
name = input("What's your name?")

#######################################################################

# Remove whitespace from str
name = name.strip()

#######################################################################

# Capitalize the first letter of the user's name
name = name.capitalize()

#######################################################################

# Divide user's name to whitespace of between first and last name
first, last = name.split(" ")
# 첫번째 값은 첫번째 변수에, 두번째 값은 두번째 변수에 저장.

#######################################################################

# Say hello to user
print(f"hello, {first}")

#######################################################################
