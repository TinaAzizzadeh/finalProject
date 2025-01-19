from django.core.mail import send_mail

def send_registration_email(user_email):
    subject = 'Welcome Message'
    message = 'Thank you for registering on our website.'
    from_email = 'eventsorojecttz@gmail.com'
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)


def send_createvent_email(user_email):
    subject = 'Welcome  Message'
    message = 'Thank you for choosing our website to representing your event! '
    from_email = 'eventsorojecttz@gmail.com'
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)



