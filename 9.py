class Notification:
    def send(self):
        pass


class Email_Notification(Notification):
    def send(self):
        return f"Email: You've got a notification"

class Sms_Notification(Notification):
    def send(self):
        return f"SMS: You've got a notification"        

en = Email_Notification()
sn = Sms_Notification()

print(f'{en.send()}\n{sn.send()}')