#DAY 15 - 16
#/(root)-starting of linux directory structure
#/bin - command line utilities like ls cp and mv
#/etc configuration files,directives -such as sshd_config and FTP vsftpd.conf
#/var variable data - system logs - such as log analyzer and regex data extractor
#/proc - A virtual directory that represents currently running processes as files - allowing you audit system activity in real time.
#/dev - hardware as files - PACKET SNIFFER INTERFACE with network drivers to intercept raw traffic
#/home - The location for user-specific data such as kali user profile u targeted during SSH Brute force audit
#/tmp - temporary files
from ensurepip import bootstrap
from os import write

from scapy.contrib.automotive.bmw.definitions import WEBSERVER
from scapy.layers.dhcp6 import DHCP6OptBootFileUrl
from scapy.tools.UTscapy import execute_campaign
from scapy.utils import tcpdump
from unicodedata import lookup
from urllib3 import connection_from_url

from file_organizer import destination_path
from port_scanner import service_name

#--TERMINAL NAVIGATION--            ALL CONF FILE                    MODIFIED IN 24HRS       LARGE FILE
   #find / -name filename     eg:   find /etc -name "*.conf"   eg:   find / -mtime -1   eg: find / -size +100M
   #grep -r 'word' /path


#--USER AND GROUPS--     ----DAY-17----
  #management commands - adduser - to add user , deluser - to remove , usermod - to modify existing account properties
#  /etc/passwd(USER DATABASE) - basic user info inside.
# /etc/shadow(PASSWORD HASHES) - mathematical fingerprints of servers passwords
# su,sudo - sudo provides temporary root privileges su allows to switch user
#THE RWX FRAMEWORK - permissions
#r - read -binary - 4
#w - write -binary - 2
#x - execute -binary - 1
#FOR EVERYTHING - 755 - owner can do anything and other can read can execute
#SUID bit  - permission from 4000
#runs with permission of owner and not with the person who launches the file - find / -perm -4000
#CONTROLLING SYSTEM ACTIVITY
 #ps aux   - provides the snapshot of every running process on the system
 #MANAGING PROCESSES
 #kill PID - stop a specific process its unique process ID  -- we could also use ctrl+c
 #killall name - stops every instance of a program
#JOB CONTROL
 #bg -  move a process to the background so it keeps running . similar to MULTITHREADING
 #fg - Brings a back grounded process back to front
 #jobs - list current background tasks


#                ----DAY 18----
#GREP - THE POWERHOUSE
 #scans the specific patterns and is essential for security auditing.
 # grep 'error' /var/log/syslog

 #FUNCTIONAL FLAGS:
 #-i caseinsensitive
 #-r recursive - search through every file in a directory and its subdirectories
 #-v invert - shows every line that does not contain the word
 #-E Extended Regex - advanced pattern symbols \d and +
#awk - COLUMN PROCESSOR
#handle structured data that is organized into columns - 10 web server logs
 #column printing - awk '{print $1}' file - prints only the first word or column of every line
 #Field Separator - (-F) - by default, awk looks for spaces. if ur auditing the /etc/passwd user database eg: -F: '{print $1}' /etc/passwd extracts only usernames.

#sed - The Stream Editor
 # sed is used for automated data sanitization and normalization.It finds text and replace it on the fly without opening the file in an editor
 #Global Substitution: sed 's/old/new/g' file replaces every occurrence of old with new
 #Range Printing: sed -n '5,10p' file    outputs only lines 5 through 10
 #line deletion: sed '/word/d' file     deletes every line containing a specific word

#PRACTICAL EXERCISES DAY 18
  #Find the Top 10 Most Common Words
#This is a standard administrative audit to find the most frequent events in a log.
#Command: cat file | tr ' ' '\n' | sort | uniq -c | sort -nr | head -10.
#Explanation: This pipes your data through a "conveyor belt": it puts every word on a new line, sorts them, counts the unique occurrences, and then shows the top 10 [373, 377, Query].
#3. Extract All IP Addresses from a Log
#You can now do this without a Python script by using the IP Pattern you built on Day 6
#.
#Command: grep -E -o "(
#{1,3}[\.]){3}
##1,3}" /var/log/syslog [238, Query].
#Logic: The -o flag tells grep to only show the "match" (the IP) rather than the whole messy log line [Query].
#4. Count Failed SSH Attempts
#Building on your Day 9 SSH Auditor work, you can see if someone is currently trying to brute-force your machine
#.
#Command: grep 'Failed password' /var/log/auth.log | wc -l [Query].

#Logic: It finds every "Failed password" event in the authentication log and passes the results to wc -l to count the total lines [Query].



#----DAY 19 ----
#BASH SCRIPTING
#STARTS WITH - #!/bin/bash
#arguments - $1
#networking tricks - /dev/tcp
#4 tools are made on linux system
#print("") - echo " "

# -- DAY 20 - 21 ---
#NETWORKING COMMANDS
#ip addr - shows all network interfaces on your machine
#ip route - shows how traffic flows out of your machine
#ss -tulpn - shows everyopen port on ur machine t - TCP u - UDP l - listen -p port n - show numbers
#curl http://site - checking if server is up and headers
#dig domain.com - deep DNS lookup
#traceroute ip - ur packets route passes and destination
#tcpdump -i eth0 - captures raw traffic on interfaces
#SERVICE MANAGEMENT
#systemctl start/stop/status service_name - controls background services and programs
#systemctl enable servicename - makes a service start everytime the machine boots
#journalctl -f - Live system log viewer f - follow
#crontab -e - Opens a sheduler when you write rules like run this script every hour
#TO START A WEBSERVER
#python3 -m http.server 8080

#---DAY 22 - 24 ---
#LOG ANALYSIS TO DETECT ATTACKERS IN REAL-TIME
#/var/log/auth.log - records every login attempt sudo command and ssh connection
#/var/log/syslog - general purpose log that captures system wide events including service  starts , hardware changes , and kernel messages
#/var/log/apache2/ - contains web server access and error logs they are used to detect automated web attacks like directory brute-forcing
#USE OF GREP IN LOGS
#grep 'Failed password' /var/log/auth.log
#grep 'Accepted password' /var/log/auth.log
#---AUTOMATED LOG PARSER---IN KALI
#TWO TYPES BASED ON AUTH.LOG PATH AND JOURNALCTL PATH
