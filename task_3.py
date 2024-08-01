# password generator
import secrets
import string

def char_password(password_length):
    n = int(password_length)
    characters=string.ascii_letters
    password = ''.join(secrets.choice(characters)for _ in range(n))
    print(" password : " , password)
    print(f"your password is '{password}' with the desired length'{n}' ")

def digit_password(password_length):
    n = int(password_length)
    digits=string.digits
    password = ''.join(secrets.choice(digits)for _ in range(n))
    print(" password : " , password)
    print(f"your password is '{password}' with the desired length'{n}' ")

def  char_digit_password(password_length):
    n = int(password_length)
    characters=string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters)for _ in range(n))
    print(" password : " , password)
    print(f"your password is '{password}' with the desired length'{n}' ")

password_length = input("Enter Password Length : ")
while True:
    
    print("1.Combination of characters password")
    print("2.Combination of digits password")
    print("3.Combination of digits and character password" )
    choice = input("Enter which type of password you want to Generate  ")
    if choice == '1' :
        char_password(password_length)
        print("        ****THANK YOU****")
        break
    elif choice =='2':
        digit_password(password_length)
        print("        ****THANK YOU****")
        break
    elif choice =='3':
        char_digit_password(password_length)
        print("       ****THANK YOU****")
        break
    else:
        print("enter valid options")
        choice = input("choose the above options")

