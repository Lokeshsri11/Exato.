from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lokeshsri1109@gmail.com'
app.config['MAIL_PASSWORD'] = 'hdxv aiua abss osly'
app.config['MAIL_DEFAULT_SENDER'] = 'lokeshsri1109@gmail.com' 

mail = Mail(app)

@app.route('/sendmail', methods=['POST'])
def send_mail():
    try:
        # Get form data
        first_name = request.form.get('First-Name')
        last_name = request.form.get('Last-Name')
        job_title = request.form.get('Job-Title')
        company_name = request.form.get('Company-Name')
        email = request.form.get('Email-id')
        phone_number = request.form.get('Phone-Number')
        how_did_you_hear = request.form.get('How-did-you-hear-about-us')
        remarks = request.form.get('Remarks')
        
        # Check captcha (you may want to implement a more secure solution)
        # captcha_input = request.form.get('captcha')
        # expected_captcha = 'your_expected_captcha_value'
        # if captcha_input != expected_captcha:
        #     return jsonify({'success': False, 'message': 'Invalid captcha'})

        # Create and send email
        subject = 'Contact Us Form Submission'
        body = f"""
        First Name: {first_name}
        Last Name: {last_name}
        Job Title: {job_title}
        Company Name: {company_name}
        Email: {email}
        Phone Number: {phone_number}
        How did you hear about us: {how_did_you_hear}
        Remarks: {remarks}
        """

        msg = Message(subject, recipients=['lokeshsri1109@gmail.com'], body=body)
        mail.send(msg)

        return jsonify({'success': True, 'message': 'Email sent successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
