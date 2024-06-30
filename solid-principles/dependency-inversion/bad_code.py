class EmailSender:
    def send_email(self, recipient, subject, body):
        # Implementation details for sending email
        pass

class NotificationService:
    def __init__(self):
        self.email_sender = EmailSender()

    def send_notification(self, user, message):
        self.email_sender.send_email(user.email, "Notification", message)


'''
In this example, the NotificationService class directly depends on the EmailSender class, which is a low-level module. This violates the Dependency Inversion Principle because the high-level NotificationService module depends on the low-level EmailSender module.

'''