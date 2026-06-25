#MODULES & LIBRARIES && PASSWORD GENERATOR && CAESAR CIPHER
import os #lets you talk to the operating system
print(os.listdir("."))
if os.path.exists("D3.py"):
    print("D3 EXISTS")
else:
    print("D3 NOT EXISTS")
import sys #TERMINAL INPUTS TO RUN COMMANDS FROM TERMINAL LIKE PYTHON D3.py 192.168.1.1
print("inputs received:" , sys.argv)
import random #anything random
random.randint(1,10)
print(random.randint(1,10))
import datetime
rightnow = datetime.datetime.now()
print(rightnow)
clean = rightnow.strftime("%Y %m %d %H %M %S")
print(clean)

#PASSWORD GENERATOR
print("----------PASSWORD GENERATOR----------")
import random
import string
length = int(input("LENGTH:"))
use_upper = input("include uppercase? (y/n)").strip().upper()
use_digits = input("include digits? (y/n)").strip().upper()
use_symbols = input("include symbols? (y/n)").strip().upper()

first_char = string.ascii_lowercase
if use_upper == "Y":
    first_char = first_char + string.ascii_uppercase
if use_digits == "Y":
    first_char = first_char + string.digits
if use_symbols == "Y":
    first_char = first_char + string.punctuation
score = 1
if use_upper == "Y": score += 1
if use_digits == "Y": score += 1
if use_symbols == "Y": score += 1
if length >= 12 and score == 4:
    strength = "strong"
elif length >= 8 and score == 3:
    strength = "medium"
else:
    strength = "weak"
password = ""
for i in range(length):
    password += random.choice(first_char)
print(password)
print(f"PASSWORD STRENGTH: {strength}")
