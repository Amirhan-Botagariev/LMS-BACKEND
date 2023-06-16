import smtplib
from email.mime.text import MIMEText

sender_email = "amirkhan1botagariev@mail.ru"
recipient_email = "ruby.mainacc@gmail.com"

subject = "Automated Email"
message = "Sucking cock."

# SMTP server configuration (example: Gmail)

smtp_server = "smtp.mail.ru"
smtp_port = 587
smtp_username = "amirkhan1botagariev@mail.ru"
smtp_password = "1YQrNi1SiAcNmC7n24pp"

msg = MIMEText(message)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)

    server.starttls()

    server.login(smtp_username, smtp_password)

    server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error sending email:", str(e))
finally:
    server.quit()

