def enviarEmail(email, senha, html_text, to_email, subject):
    import os
    import smtplib
    from email.message import EmailMessage



    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to_email
    msg.add_alternative(f"""
        \
       {html_text}
    """, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email, senha)
        smtp.send_message(msg)
