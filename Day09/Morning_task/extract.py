# A1: Extract emails and phone numbers from text using re

import re

sample_text = """
Welcome to Green Corner Community Garden!
For volunteer days, email Priya at priya@greencorner.org.
Questions about workshops? Write to hello@greencorner.org or
events@greencorner.co.uk.
Call us at +1-800-555-0199 or 077-1234-5678.
Our garden office number is 020-7946-0958.
"""

# Email pattern
email_pattern = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'

# Phone pattern (handles various formats)
phone_pattern = r'(\+?\d[\d\s\-().]{7,}\d)'

emails = re.findall(email_pattern, sample_text)
phones = re.findall(phone_pattern, sample_text)

print("=== Emails Found ===")
for email in emails:
    print(f"  {email}")

print("\n=== Phone Numbers Found ===")
for phone in phones:
    print(f"  {phone.strip()}")
