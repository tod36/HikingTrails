from django.core.mail import send_mail

def send_welcome_email(user):
    send_mail(
        subject="Welcome to HikingTrails!",
        message="Thank you for signing up for HikingTrails! We hope you enjoy our app!",
        from_email="todor36@gmail.com",
        recipient_list=[user.email],
        fail_silently=False,
    )