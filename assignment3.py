# Assignment: Regex Validator for Email IDs and IPv4 Addresses
# Build a Python program that validates and extracts email IDs and IPv4 addresses from text using regular expressions.
# The goal is to demonstrate understanding of Python’s re module, regex anchors, character classes, groups, non-capturing groups, alternation, and validation using re.fullmatch() / re.findall().
# Problem Statement
# Create a Python file named regex_validator.py that implements the following functions:
 
# def is_valid_email(email: str) -> bool:     passdef is_valid_ipv4(ip: str) -> bool:     passdef extract_emails(text: str) -> list[str]:     passdef extract_ipv4_addresses(text: str) -> list[str]:     pass
# Email Validation Rules
# A valid email should follow these rules:
# Must contain exactly one @.
# Username/local part can contain:
# Letters
# Digits
# Dot .
# Underscore _
# Percent %
# Plus +
# Hyphen -
# Username should not start or end with a dot.
# Username should not contain consecutive dots.
# Domain should contain at least one dot.
# Domain name can contain letters, digits, and hyphens.
# Domain labels should not start or end with a hyphen.
# Top-level domain should contain only letters and must be at least 2 characters.
# Spaces are not allowed.
# Examples of valid emails:
 
# john.doe@example.com admin+test@company.co.in user_name@sub.domain.org test123@my-domain.com
# Examples of invalid emails:
 
# john..doe@example.com .john@example.com john.@example.com john@example john@.com john@example..com john@-example.com john@example.c john example@test.com
# IPv4 Validation Rules
# A valid IPv4 address should follow these rules:
# Must contain exactly 4 octets separated by dots.
# Each octet must be a number from 0 to 255.
# No alphabetic characters are allowed.
# No empty octets are allowed.
# No extra leading/trailing characters are allowed.
# Leading zeros should not be allowed, except for the value 0.
# Examples of valid IPv4 addresses:
 
# 192.168.1.1 10.0.0.5 0.0.0.0 255.255.255.255 172.16.254.1
# Examples of invalid IPv4 addresses:
 
# 256.1.1.1 192.168.1 192.168.1.1.5 192.168..1 01.2.3.4 abc.def.ghi.jkl 123.456.78.90
# Extraction Requirements
# Given a block of text, the program should extract all valid emails and IPv4 addresses.
# Example input:
 
# User john.doe@example.com logged in from 192.168.1.10. Backup admin+test@company.co.in accessed 10.0.0.5. Invalid email: john..doe@example.com Invalid IP: 999.10.10.10
# Expected output:
 
# Emails: ['john.doe@example.com', 'admin+test@company.co.in'] IPv4 Addresses: ['192.168.1.10', '10.0.0.5']
# Restrictions
# Use Python’s built-in re module.
# Do not use external validation libraries.
# Do not use Python’s ipaddress module for IPv4 validation.
# Use re.fullmatch() for validation functions.
# Use re.findall() or re.finditer() for extraction functions.
# Add comments explaining your regex. 

import re

EMAIL_REGEX = re.compile(
    r"^(?!.*\.\.)"                       
    r"[A-Za-z0-9_%+-]+(?:\.[A-Za-z0-9_%+-]+)*" 
    r"@"                                 
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+"  
    r"[A-Za-z]{2,}$"                     
)

OCTET = (
    r"(?:25[0-5]|"      
    r"2[0-4][0-9]|"      
    r"1[0-9]{2}|"       
    r"[1-9][0-9]?|"     
    r"0)"                
)
IPV4_REGEX = re.compile(rf"^{OCTET}\.{OCTET}\.{OCTET}\.{OCTET}$")


def is_valid_email(email: str) -> bool:
    return re.fullmatch(EMAIL_REGEX, email) is not None


def is_valid_ipv4(ip: str) -> bool:
    return re.fullmatch(IPV4_REGEX, ip) is not None


def extract_emails(text: str) -> list[str]:
    candidates = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return [email for email in candidates if is_valid_email(email)]


def extract_ipv4_addresses(text: str) -> list[str]:
    candidates = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)
    return [ip for ip in candidates if is_valid_ipv4(ip)]


if __name__ == "__main__":
    sample_text = """
    User john.doe@example.com logged in from 192.168.1.10.
    Backup admin+test@company.co.in accessed 10.0.0.5.
    Invalid email: john..doe@example.com
    Invalid IP: 999.10.10.10
    """

    print("Emails:", extract_emails(sample_text))
    print("IPv4 Addresses:", extract_ipv4_addresses(sample_text))

