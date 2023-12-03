from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.ethereal.email'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mekhi.deckow@ethereal.email'
app.config['MAIL_PASSWORD'] = 'pkg9q4bd1aK2AtBwg5'

mail = Mail(app)

@app.route('/sendmail', methods=['POST'])
def send_mail():
    data = request.json

    first_name = data.get('First-Name', '')
    last_name = data.get('Last-Name', '')
    job_title = data.get('Job-Title', '')
    company_name = data.get('Company-Name', '')
    email_id = data.get('Email-id', '')
    phone_number = data.get('Phone-Number', '')
    how_did_you_hear_about_us = data.get('How-did-you-hear-about-us', '')
    remarks = data.get('Remarks', '')

    # Configure the Flask-Mail Message
    message = Message('New Contact Form Submission',
                      sender='mekhi.deckow@ethereal.email',
                      recipients=['lokeshsri1109@gmail.com'])

    message.body = f"""
        First Name: {first_name}
        Last Name: {last_name}
        Job Title: {job_title}
        Company Name: {company_name}
        Email: {email_id}
        Phone Number: {phone_number}
        How did you hear about us: {how_did_you_hear_about_us}
        Remarks: {remarks}
    """

    try:
        # Send the email
        mail.send(message)
        return jsonify({'message': 'Email sent successfully'}), 200
    except Exception as e:
        print(f'Error sending email: {e}')
        return jsonify({'message': 'Error sending email'}), 500

if __name__ == '__main__':
    port = 3300
    app.run(port=port, debug=True)
