#PS
#Building on top of the conditional exercise, write a script that will loop through a list of users,
#where each item is a user dictionary from the previous exercise, printing out each user’s status on a separate line.
#Additionally, print the line number at the beginning of each line, starting with line 1.
#Be sure to include a variety of user configurations in the users list.

#User Keys:
#'admin' - a boolean representing whether the user is an admin user.
#'active' - a boolean representing whether the user is currently active.
#'name' - a string that is the user’s name.
#Depending on the values of the user, print one of the following to the screen when you run the script:

#print (ADMIN) followed by the user’s name if the user is an admin.
#print ACTIVE - followed by the user’s name if the user is active.
#print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active.
#print the user’s name if neither active nor an admin.
#--------------------------------------------------------------------------------------------------------------------------------------

#!/usr/local/bin/python
user1 = {'admin':True, 'active':True, 'name':'Amit'}
user2 = {'admin':True, 'active':False, 'name':'ABC'}
user3 = {'admin':False, 'active':True, 'name':'PQR'}
user4 = {'admin':False, 'active':False, 'name':'XYZ'}
list = [user1, user2, user3, user4]
line = 1
for user in list:
    if user['admin'] and user['active']:
        print('%s Admin and Active user is %s' % (line, user['name']))
    elif user['admin']:
        print('%s Only admin user is %s' % (line, user['name']))
    elif user['active']:
        print('%s Only active user is %s' % (line, user['name']))
    else:
        print('%s Neither admin nor active user is %s' % (line, user['name']))
    line += 1

#>>Output
#bin $ ./thirdExercise.py
#1 Admin and Active user is Amit
#2 Only admin user is ABC
#3 Only active user is PQR
#4 Neither admin nor active user is XYZ
