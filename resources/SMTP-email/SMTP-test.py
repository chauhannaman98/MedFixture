import smtplib, random, string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

toaddrs = input("Enter your email ID: ")
username = 'techmirtzskbuddy@gmail.com'
password = 'passwordnahihai'
x = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

message = MIMEMultipart("alternative")
message["Subject"] = "Forgot Password | MedFixture"
message["From"] = username
message["To"] = toaddrs

html = """\
<html>
	<body>
		<h1 align="center">Hi! Seems like you forgot you password. </h1>
			<p align="center">Don't worry! Just enter the verification code
                given below.</p>
            <p align="center">Your verification code is <code>"""+ x +"""</code></p>
    </body>
    <footer align="center">Project maintained by 
        <a href="https://github.com/chauhannaman98">chauhannaman98</a></footer>
</html>
"""

part1 = MIMEText(html, "html")
message.attach(part1)


try:
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(username, toaddrs, message.as_string())
except Exception as e:
	print(e)
finally:
	server.quit()

in_code = input("Enter the verification code: ")
if in_code == x:
	print("Verification successful")
else:
	print("Enter correct verification code")