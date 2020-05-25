import smtplib, random, string
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

toaddrs = input("Enter your email ID: ")
username = 'techmirtzskbuddy@gmail.com'
password = 'passwordnahihai'
x = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

message = MIMEMultipart("alternative")
message["Subject"] = "Forgot Password | MedFixture"
message["From"] = username
message["To"] = toaddrs

# fp = open('icon.png', 'rb')
# msgImage = MIMEImage(fp.read())
# fp.close()

# # Define the image's ID as referenced above
# msgImage.add_header('Content-ID', '<logo>')
# msgRoot.attach(msgImage)

html = """\
<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>Forgot Password | MedFixture</title>

<body>
    <p align="center" style="text-align: center;font-size: larger;">
        <img src="https://raw.githubusercontent.com/chauhannaman98/MedFixture/master/resources/icon.png" alt="Logo" width="80" height="80">
        <h3 align="center">MedFixture</h3>
    </p>
    <h1 align="center">Hi! Seems like you forgot your password. </h1>
        <p style="text-align: center;font-size: larger;">Don't worry! Just enter the verification code
            given below.</p>
        <p style="text-align: center;font-size: larger;">Your verification code is :</p>
        <p class="veri-code" style="text-align: center;font-size: larger;font-family: 'Inconsolata', monospace;">"""+ x +"""</p>
</body>
<footer style="text-align: center;">
    <ul style="list-style-type: none;padding: 0;margin: 0;" , margin="0," padding="0">
        <li style="font-size: smaller;">An open-source project maintained by <a href="https://github.com/chauhannaman98">chauhannaman98</a></li>
        <li style="font-size: smaller;"><a href="https://chauhannaman98.github.io/MedFixture">Visit website</a></li>
    </ul>
</footer>
</html>
"""

part1 = MIMEText(html, "html")
message.attach(part1)
print("Message built")

try:
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	print("Logged in")
	server.sendmail(username, toaddrs, message.as_string())
	print("Verification code sent")
except Exception as e:
	print(e)
finally:
	server.quit()

in_code = input("Enter the verification code: ")
if in_code == x:
	print("Verification successful")
else:
	print("Enter correct verification code")