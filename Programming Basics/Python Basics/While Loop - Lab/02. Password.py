user = input()
password = input()

login_attempt_pw = input()
while login_attempt_pw != password:
    login_attempt_pw = input()
print(f"Welcome {user}!")
