#REGEX EXTRACTOR IS A SEARCH ENGINE OF A FILE SEARCH FOR SPECIFIC TEXT FROM FILE
#text.find("apple")
#\d - digits(0-9)          \d+ - More than one digit grp or bunch-of numbers
#\w - word char number underscore
#\s - space
#.  - WildCard
#*  - 0 or more times
#?  - 0 or one time
#{min, max} - \d{1,3}
#IP ======   \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}
#IP ======    192   .168    .1      .55
import re
ip_pattern = r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}"
email_pattern = r"[\w\.-]+@[\w\.-]+[a-zA-Z]{2,4}"
url_pattern = r"https?://[^\s]+"
with open("raw_logs.txt","r", encoding="utf-8") as file:
    content = file.read()
print("==========================================")
print("      REGEX SECURITY DATA EXTRACTION      ")
print("==========================================")

extracted_ips = re.findall(ip_pattern, content)
extracted_emails = re.findall(email_pattern, content)
extracted_urls = re.findall(url_pattern, content)

print("\n[+] Extracted IP ADDRESSES:")
for ip in extracted_ips:
     print(f" ---{ip}")
print("\n[+]Extracted Email ADDRESSES:")
for email in extracted_emails:
    print(f" ---{email}")
print("\n[+]Extracted URL ADDRESSES:")
for url in extracted_urls:
    print(f" ---{url}")
print("===============================================")