#pip install Flask
from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets 

app = Flask(__name__)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email'] 

        verification_code = secrets.token_hex(4)
      
        send_verification_email(email, verification_code)


        return "Email verify sent" + email
    return render_template('register.html')
def send_verification_email(user_email, verification_code):
    email = "your_email@gmail.com"  
    password = "your_password"      
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = user_email
    msg['Subject'] = "verify email "

    message = f"hello,\n\nUsing code to verify email: {verification_code}\n\nThanks,\nLovely"
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    app.run(debug=True)
