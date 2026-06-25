#ord() and chr() convert char into number and vice versa
import string
print("--CAESAR CIPHER ENGINE--")
print("1. encrypt a text")
print("2. decrypt a text")
print("3. Brute force a text")
choice = input("ENTER CHOICE: ")
msg = input("ENTER TEXT:")
if choice == "1" or choice == "2":
    shift = int(input("ENTER SHIFT NUMBER: "))
    if choice == "2":
        shift = -shift

    output_msg = ""
    for char in msg:
            if char.islower():
                new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
                output_msg += new_char
            elif char.isupper():
                new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
                output_msg += new_char
            else:
                output_msg += char
            print(f"THE NEW TEXT IS {output_msg}")

if choice == "3":
    print("RUNNING BRUTE FORCE")

    for shift in range(1, 26):
       decrypted_msg = ""
       for char in msg:
           if char.islower():
             new_char = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
             decrypted_msg += new_char
           elif char.isupper():
             new_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
             decrypted_msg += new_char
           else:
             decrypted_msg += char
       print(f"Key {shift:02d}: {decrypted_msg}")

