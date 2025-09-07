from celery import shared_task

@shared_task
def send_welcome_email(user_email):
    # print a mock email sending process
    print(f"Sending welcome email to {user_email}")
    return f"Email sent to {user_email}"
