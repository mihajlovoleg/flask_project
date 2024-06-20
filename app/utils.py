from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.config import SEND_GRID_API_CLIENT

def send_email(to_email, subject, content):
    message = Mail(
        from_email='mihajlovaoleg@gmail.com',
        to_emails=to_email,
        subject=subject,
        html_content=content)
    
    try:
        sg = SendGridAPIClient(SEND_GRID_API_CLIENT)
        response = sg.send(message)
        print(f"Email sent with status code {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")