#!/usr/bin/python3

import random
print('''
=============================================================================            

 ____                                     _   __  __       _             
|  _ \ __ _ ___ _____      _____  _ __ __| | |  \/  | __ _| | _____ _ __ 
| |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |\/| |/ _` | |/ / _ \ '__|
|  __/ (_| \__ \__ \\\ V  V / (_) | | | (_| | | |  | | (_| |   <  __/ |   
|_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| |_|  |_|\__,_|_|\_\___|_|   
                          
                        By Michael Johnson                                               

=============================================================================
''')
print('''
Pro Tip:
======== 

Make your password at least 30 characters in length. 
Password cracking software available to most of us is not able to crack those kinds of passwords easily.

========
''')

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()_-+=[]\{}|;',./:<>?'`"

x = input("How Many Passwords Would You Like To Make? ")
x = int(x)

y = input("What Length Would You Like Your Password/s? ")
y = int(y)

print("\nYour Passwords:\n")

for p in range(x):
    password = ''
    for c in range(y):
        password += random.choice(chars)
    print(password)

print('''
========

Thank you for using Password Maker.

Goodbye ^.^

========
''')

# A special thanks to https://trinket.io/python/08c0ad3359 for offering the base code for which this code was built. Origato.


