# Chapter 5 - If statements
# Exercises: 
# Checking for special users (admin)


users = ['scott', 'pitt', 'dowwas','admin', 'louis', 'trek', 'mack']

if users:
    for user in users:
        if user == 'admin':
            print(f"Welcome back {user.title()}, would you like to see the status report?")
        else:
            print(f"Welcome back {user.title()}!")
else:
    print('We need to find some users!')
