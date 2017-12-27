#PS
#Write a Python script that sets the following variables:

#first_name - Set to your first name
#last_name - Set to your last name
#age - Set to your age as an integer
#birth_date - Set to your birthdate as a string
#Using the variables, print the following to the screen when you run the script:

#My name is FIRST_NAME LAST_NAME.
#I was born on BIRTH_DATE and I'm AGE years old.
#-------------------------------------------------------------------------------------------------------------------------------

#!/usr/local/bin/python
first_name = 'Amit'
last_name = 'Prajapati'
age = 27
birth_date = '30-Aug-1991'

print("My name is %s %s,\nI was born on %s and I am %s years old" % (first_name, last_name, birth_date, age))

#>>Output
#bin $ ./firstExercise.py
#My name is Amit Prajapati,
#I was born on 30-Aug-1991 and I am 27 years old
