# DAY 33 - 28 SEP 2026
#DNS -DOMAIN NAME SYSTEM
#  -Computers do not communicate using human-friendly names like google.com they communicate using numerical IP addresses like 142.250.190.46(IPv4) or (IPv6)
#  -Internet's global translation directory, Whenever you type a website name or a web address into your browser your device sends a DNS query to translate that text name into numerical IP address.
#  -Why DNS IS Important for hackers?
 # DNS is frequently called "hackers fav target" because of two keys security realities.
#   -Reconnaissance and footprinting - Before a target your need to map out what servers they own by querying DNS records, an auditor can reveal the company's mail servers authoritative nameservers internal subdomains and external IP ranges.
#   -Traffic Hijacking - if an attacker can spoof or corrupt a DNS record every user attempting to visit a legitimate website or send an email can be silently rerouted to an attacker controlled server.
   
#DNS Record Types 
# DNS zones store information using specific Record Types. Each record type serves a dedicated routing or verification purpose
#    A - Record Address
# AAAA - Record IPv6   
#   MX - Record Mail Exchange
#CNAME - Record Canonical Name
#  TXT - Record Text
#   NS - Name server
#  PTR - Pointer Record


#DNS Tools in kali linux 
 #-Dig - primary command line tool used for pentesting and network engineers for DNS queries. Provies raw DNS server responses.
 #-nslookup - is a lightweight cross platform tool used for quick simple dns queries

#DNS ATTACKS 
# -DNS Spoofing - an attacker sends fake DNS responses to a victim machine before the legitimate DNS server can respond.
# -DNS Cache Poisoning - Corrupting th ecached memory database of a recursive DNS resolver(such as an ISP's DNS server or a corporate DNS server)
# -DNS Zone Transfer(AXFR) - is an administrative protocol command used to replicate an entire DNS zone file from a primary nameserver to a secondary nameserver.

