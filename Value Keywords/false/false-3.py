is_logged_in = False

user_input = input("Enter 'login' to log in: ")

if user_input.lower() == "login":
    is_logged_in = True

if is_logged_in:
    print("Welcome! You are now logged in.")
else:
    print("Please log in to continue")
