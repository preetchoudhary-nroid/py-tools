#DAY 6 OOPS BASICS && REGEX REGULAR EXPRESSIONS && NETWORK INFO SCANNER
#OOPS INCLUDE CLASS AND def __init__(self,) constructor
#attributes -- name,severity,status
#methods -- apply_patch(),display_advisory
class vulnerability:
    def __init__(self, name, severity, cve_id, description):
        self.name = name
        self.severity = severity.upper()
        self.cve_id = cve_id
        self.description = description

        self.is_patched = False
    def display_advisory(self):
        if self.is_patched:
            status = "SECURE (The patch has been Deployed)"
        else:
            status = "VULNERABLE(The Action is Required Immediately)"
        print("\n"+"="*50)
        print(f"SECURITY ADVISORY | {self.cve_id}")
        print("="*50)
        print(f"Vulnerability: {self.name}")
        print(f"RISK SEVERITY LEVEL: {self.severity}")
        print(f"Current Status:{status}")
        print(f"Threats Details:{self.description}")
        print("="*50)
    def apply_patch(self):
        self.is_patched = True
        print(f"[+]SYSTEM ACTION: successfully deployed security patch for {self.cve_id}")

#WORKING WITH THE OBJECTS
vuln1 = vulnerability(
    name="Log4Shell",
    severity="Critical",
    cve_id = "CVE-2021-44228",
    description="Remote code execution vulnerability inside Apache Log4j loggers."
 )
vuln2 = vulnerability(
    name="LogCrush",
    severity="Medium",
    cve_id = "CVE-2026-9999",
    description="Denial of Service attack via remote memory consumption"
 )
vuln1.display_advisory()
vuln2.apply_patch()
vuln2.display_advisory()
