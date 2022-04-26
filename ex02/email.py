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

html_msg =  '''<html>
        <h1>Parabéns! Você acaba de comprar um carro de mão!</h1>
        <ul>
            <li>Marca: Ford</li>
            <li>Modelo: DiMão</li>
            <li>Ano: 2022</li>
        </ul>
        <p>Obrigado pela preferência!</p>
        <p><strong>Concessionária Sol Quente</strong></p>
        </html>'''


if __name__ == '__main__':
    enviarEmail('concessionariasolquente@gmail.com','solquente13',html_msg,'brenixkts@gmail.com','Compra de carro efetuada')



