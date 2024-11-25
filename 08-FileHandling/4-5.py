from emails import email_sender, email_recipient, email_subject, email_body

with open('email.txt', 'r', encoding='utf-8') as file:
    email_content = file.read()

print("Sender:", email_sender(email_content))
print("Recipient:", email_recipient(email_content))
print("Subject:", email_subject(email_content))
print("Body:\n", email_body(email_content))
