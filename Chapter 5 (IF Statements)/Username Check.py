# Chapter 5 - If statements
# Exercises: 
# - Case insensitive username availability

current_users = ['john', 'eric', 'smith', 'topo', 'iuno']
new_users = ['Smith', 'doss', 'holler', 'iuno', 'Topo']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print(f"The username {new_user} is unavailable!")
        else:
            print(f"The username {new_user} is available!") 
