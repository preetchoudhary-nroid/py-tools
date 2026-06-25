#conditional & loops &  functions
#LISTS AND DICTIONARIES & FILE HANDLING & ERROR HANDLING AND STRING METHODS
#conditional are used for making decisions
#if elif else      = ASSIGNS A VARIABLE AND == IS EQUAL TO
#!= NOT EQUAL TOO <= >=
#COMBINING CONDITIONS AND , OR , NOT
runs = 43
if runs > 0:
    print("RUNS ARE MORE THAN ZERO")
elif runs == 0:
    print("NO RUNS ARE MADE")
else:
    print("player ABSENT")
player = "kohli"
if player == "kohli" and runs > 0:
    print("kohli has just started")
elif player != "kohli" and runs > 0:
    print("PLAYER IS NOT KOHLI")
else:
    print("PLAYER IS ABSENT")
#loops prevents hard and complex code
#for - if u have the range
for i in range(1,5):
    print(f"{i} runs")
for letter in "kohli":
    print(letter.upper())
#while loop - run until condition becomes false
marks = 55
while marks >= 0:
    print(f"{marks} marks  are given ")
    marks -= 5
    if marks <= 0:
        break
#functions: reusable code blocks
def student_name():
    return "Preet Choudhary"
print(f"{student_name()} has got this {marks}")



#example - automated e-commerce checkout
def check_user():
  username = ("preet")
  username = username.strip()

  if username.isalpha():
    return username.capitalize()
  else:
      return "Guest"
customer = check_user()
print(f"{customer} WELCOME!! ")

price = 150
quantity = 3
subtotal = price * quantity
#0.10% tax
total = subtotal * 1.10
if total >= 200:
    shipping = 0
else:
    shipping = 15
total = total + shipping
print(f"{total} is amount to pay with shipping charges of {shipping} rupees")
#LISTS AND DICTIONARIES
#LISTS[] - numbered shopping list starting at zero
targets = [ "ip_address" , "firewall" , "database" ]
targets.append("router")
targets.remove("firewall")
#pop() - pops out the specific target and deletes it.
popped_items  = targets.pop(0)
print(f"{popped_items} is popped out of {targets}")
targets.sort() #SORT HELPS TO ARRANGE THE LIST ALPHABETICALLY CHANGES THE LIST INSIDE IT.
print(targets)
#DICTIONARIES - USE KEYS TO FIND THINGS AND IT'S VALUE
SERVER = {
    "ip":"192.168.56.103",
    "status":"Active",
    "ports": 4
}
print(SERVER["ip"])#remember the syntax to call A PARTICULAR KEY
#ADD AND UPDATE SERVER
SERVER["status"] = "DOWN"
SERVER["OS"] = "KALI LINUX"
#DELETE BY DEL
del SERVER["ports"]
for key,value in SERVER.items():
    print(f"{key} is {value}")

#FILE HANDLING
# r for read only
# w for write - destroy everything entirely
# a for append - write from ending does not destroy the file
#x for exclusive - creates a brand-new file
with open("targets.txt","w") as f:
    f.write("192.168.56.101\n")
    f.write("192.168.56.105\n")
with open("targets.txt","r") as f:
 for line in f:
    print(line)
#ERROR HANDLING AND STRING METHODS
#try - to stop crash make it inside a try block
#except - error happens in try block python immediately stops and jumps to here to handle things.
#else - runs only if try block succeeded
#finally - runs does not matter if error happened or not.
#

#VALUE ERROR
    try:
        age = int(input("enter age"))
        print(age)
    except ValueError:
         print("ENTER A VALID AGE")
#FileNotfoundError
#it happens when u try to open r
    try:
        with open("secret_password.txt","r") as f:
            print(f.read())
    except FileNotFoundError:
             print("THERE IS NO FILE OF THIS NAME")
#IndexError - grab item from list that does not exist
    tools = ["Nmap" , "wireshark"]
    try:
        print(tools[6])
    except IndexError:
        print("ERROR ON INDEX KEYS OF TOOL")
#EXAMPLE 2-----------use dictionaries to count a thing twice
network_logs ={"192.168.1.1":"1" , "192.168.1.2":"2" , "192.168.1.3":"3"}
ip_counts = {}
try:
    with open("network_logs.txt", "r") as f:
        ip_counts = {}

        for line in f:
            ip = line.strip()
            if ip in ip_counts:
                ip_counts[ip] += 1
            else:
                ip_counts[ip] = 1

    for ip, count in ip_counts.items():
        if count > 2:
            print(f"[ALERT] SUSPICIOUS  ACTIVITY FROM {ip}! appeared {count} times")
except FileNotFoundError:
       print("Error: file logs not found")