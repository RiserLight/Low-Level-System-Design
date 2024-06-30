from abc import ABC, abstractmethod

class EmailSender(ABC):
    @abstractmethod
    def send_email(self, recipient, subject, body):
        pass

class SMTPEmailSender(EmailSender):
    def send_email(self, recipient, subject, body):
        # Implementation details for sending email using SMTP
        print(f"Sending email to {recipient} with subject '{subject}' and body '{body}'")

class NotificationService:
    def __init__(self, email_sender: EmailSender):
        self.email_sender = email_sender

    def send_notification(self, user, message):
        self.email_sender.send_email(user['email'], "Notification", message)


smtp_email_sender = SMTPEmailSender()
notification_service = NotificationService(smtp_email_sender)
user = {"email": "user@example.com"}
notification_service.send_notification(user, "This is a test notification.")