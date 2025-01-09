def get_user_key():
    return input("Please Enter Key to enter program: ").strip().upper()

while True:
    user_key = get_user_key()
    if user_key == "KEY": 
        print("You have entered the proper key. Thank you!")
        break
    else:
        print("This is not a correct input. Please try again.")
