import yagmail

# Email credentials
EMAIL_USER = 'test24@gmail.com'
EMAIL_PASS = 'password'


def send_email(email_user, email_pass, email_to, email_subject, email_body):
    """
    Send email to the email_to address with the email_subject and email_body
    """
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body)
    print('Email sent to {}'.format(email_to))


def send_email_with_attachment(email_user, email_pass, email_to, email_subject,
                               email_body, attachment):
    """
    Send email to the email_to address with the email_subject and email_body
    """
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body, attachments=attachment)
    print('Email sent to {}'.format(email_to))


def send_email_with_multiple_attachments(email_user, email_pass, email_to,
                                         email_subject, 
                                         email_body, attachments):
    """
    Send email to the email_to address with the email_subject and email_body
    """
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body, attachments=attachments)
    print('Email sent to {}'.format(email_to))


def send_email_with_multiple_recipients(email_user, email_pass,
                                        email_to, email_subject, 
                                        email_body, attachments):
    """
    Send email to the email_to address with the email_subject and email_body
    """
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body, attachments=attachments)
    print('Email sent to {}'.format(email_to))


def send_email_with_multiple_recipients_and_cc(email_user, email_pass, email_to, 
                                               email_subject,
                                               email_body, attachments):
    """
    Send email to the email_to address with the email_subject and email_body
    """
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body, attachments=attachments)
    print('Email sent to {}'.format(email_to))


def send_email_with_multiple_recipients_and_cc_and_bcc(email_user, email_pass, email_to,
                                                       email_subject, email_body, attachments):
    """
    Send email to the email_to address with the email_subject and email_body
    """
    yag = yagmail.SMTP(email_user, email_pass)
    yag.send(email_to, email_subject, email_body, attachments=attachments)
    print('Email sent to {}'.format(email_to))



send_email(EMAIL_USER, EMAIL_PASS, 'Dominic',
           'yeboahd24@gmail.com', 'Hello World')
