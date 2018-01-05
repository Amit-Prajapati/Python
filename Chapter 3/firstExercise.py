>>P.S - 
Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:

Prompts the user for a message to echo
Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
Defines a function that takes a message and count, then prints the message that many times.
To end the script, call the function with the user-defined values to print to the screen.
---------------------------------------------------------------------------------------------------------------------------------------
#!/usr/local/bin/python

def msgPrint(message, count):
    for i in range(count):
        print(message)
    return()

message = raw_input("Which message would you like to print? ")
count = raw_input("How many times you want to print the message? ").strip()
if count:
    count = int(count)
else:
    count = 1
msgPrint(message, count)
----------------------------------------------------------------------------------------------------------------------------------------

>>Output - 
chapter3 $ ./firstExercise.py
Which message would you like to print? firstExercise
How many times you want to print the message? 3
firstExercise
firstExercise
firstExercise
