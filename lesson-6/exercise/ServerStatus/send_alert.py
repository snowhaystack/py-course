import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

gmail_user = 'xxxx@gmail.com'
gmail_password = 'xxxxx'


def send_email(ip_address, status, timems, email_to):
    
    check_up = lambda val: "UP" if val else "DOWN"
    html = f"<html><body>The Host is {check_up(status)} with ms {timems} AND WE NEED A COFFEEEEEEE</body></html>"
    message_html = MIMEText(html, "html")
    message_image = MIMEImage(open(r"c:\temp\logo.jpg","rb").read())
    message_pdf = MIMEApplication(open(r"c:\temp\example.pdf","rb").read(), Name="test.pdf")

    message = MIMEMultipart()
    message.attach(message_html)
    message.attach(message_pdf)
    message["From"] = gmail_user
    message["To"] = email_to
    message["Subject"] = f"Monitor: The Host is {status} with ms {timems}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_user, gmail_password)
        server.ehlo()
        server.send_message(message)
