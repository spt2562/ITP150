current_users = ['Becca','tiffany','nat','debbie','siya']
new_users = ['Grace','Tiffany','Nat','Max','Bryan']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + ", that name is taken. Please enter a new username.")
    else:
        print("Awesome, " + new_user + " is still available.")