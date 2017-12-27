#PS: 
#Create a script that has a single variable you can set at the top called user. This user is a dictionary containing the keys:

#'admin' - a boolean representing whether the user is an admin user.
#'active' - a boolean representing whether the user is currently active.
#'name' - a string that is the user’s name.
#Example:
#user = { 'admin': True, 'active': True, 'name': 'Kevin' }
#Depending on the values of user, print one of the following to the screen when you run the script:

#print (ADMIN) followed by the user’s name if the user is an admin.
#print ACTIVE - followed by the user’s name if the user is active.
#print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active.
#print the user’s name if neither active nor an admin.
#------------------------------------------------------------------------------------------------------------------------------------

#!/usr/local/bin/python
user = {'admin':True, 'active':True, 'name':'Amit'}
if user['admin'] and user['active']:
    print('Active - (Admin) %s' % user['name'])
elif user['admin']:
    print('Admin %s' % user['name'])
elif user['active']:
    print('Active %s' % user['name'])
else:
    print(user['name'])

>>Output
bin $ ./secondExercise.py
Active - (Admin) Amit
