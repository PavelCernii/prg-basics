import re

def email_sender(content):
    match = re.search(r"From: .*<(.+)>", content)
    return match.group(1) if match else None

def email_recipient(content):
    match = re.search(r"To: .*<(.+)>", content)
    return match.group(1) if match else None

def email_subject(content):
    match = re.search(r"Subject: (.+)", content)
    return match.group(1) if match else None

def email_body(content):
    match = re.search(r"\r?\n\r?\n(.+)", content, re.DOTALL)
    return match.group(1).strip() if match else None
