'''The program always terminates if the program execution reaches 
the bottom of the instructions'''
'''how ever we can cause the program to terminate, or exit before
the last instruction by calling sys.exit() function.Since this 
function is in sys module,we have to import sys before our program
can use it'''

import sys

while True:
    print('Type exit to exit.')
    response=input()
    if response == 'exit':
        sys.exit()
    print(' you typed ' + response + '.' )
    
#infinite loop with no break statement in this program 
#the only way to exit the loop is if condition reaches the sys.exit()