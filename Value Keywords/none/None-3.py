def find_user(name, user_list):
    for user in user_list:
        if user == name:
            return user
        return None
    
users = ["Alice", "Bob"]
print(find_user("Charlie", users)) # Putput: None