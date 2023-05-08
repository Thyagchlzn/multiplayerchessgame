import smtplib
try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('thiyagarajansethu2002@gmail.com','bkonpsdkiaprnrvk')

    server.sendmail('thiyagarajansethu2002@gmail.com','thyagchlzn@gmail.com',"mail chcking")
    print("successful")
    server.quit()
except:
    print("unsuccessful")