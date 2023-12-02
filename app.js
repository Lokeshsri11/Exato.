const express = require('express');
const path = require('path');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');

const app = express();

app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Define a route to handle the form submission
app.post('/sendmail', (req, res) => {
  const { body } = req;
  const {
    'First-Name': First_Name,
    'Last-Name': Last_Name,
    'Job-Title': Job_Title,
    'Company-Name': Company_Name,
    'Email-id': Email_id,
    'Phone-Number': Phone_Number,
    'How-did-you-hear-about-us': How_did_you_hear_about_us,
    Remarks
  } = body;

  // Continue processing the form
  // Configure the nodemailer transporter
  const transporter = nodemailer.createTransport({
    service: 'ethereal',
    auth: {
      user: 'mekhi.deckow@ethereal.email',
      pass: 'pkg9q4bd1aK2AtBwg5'
    }
  });

  // Define the email options
  const mailOptions = {
    from: 'email',
    to: 'lokeshsri1109@gmail.com',
    subject: 'New Contact Form Submission',
    text: `
      First Name: ${First_Name}
      Last Name: ${Last_Name}
      Job Title: ${Job_Title}
      Company Name: ${Company_Name}
      Email: ${Email_id}
      Phone Number: ${Phone_Number}
      How did you hear about us: ${How_did_you_hear_about_us}
      Remarks: ${Remarks}
    `
  };

  // Send the email
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error('Error sending email:', error);
      res.status(500).send('Error sending email');
    } else {
      console.log('Email sent:', info.response);
      res.status(200).send('Email sent successfully');
    }
  });
});

// Start the server
const port = 3300;
app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
