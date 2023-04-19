# Importo las librerías con las cuales vamos a trabajar
import pandas as pd
import smtplib
from email.message import EmailMessage

# importamos los datos

datos = pd.read_csv('datos.csv')


# Enviamos correo electrónico para ello usamos smtplib

# Configuramos los parámetros

remitente = 'mercado.isaacpablor@gmail.com'
password = 'caahdydzivvgikqf'
asunto = 'feliz semana'
cuerpo = 'Espero que tengas una hermosa semana, recuerda que siempre podes contar con nos para lo que creas necesario. Esta empresa y yo personamente, estoy muy agradecido por tu trabajo y todo el esfuerzo que realizas cada día. Siempre queremos vvalorar eso y hacertelo saber. Te mando un abrazo y espero tenga una jornada increible! Se te quiere.'

# Recorrer el DataFrame y enviar un correo electrónico a cada destinatario
for i, fila in datos.iterrows():
    destinatario = fila['correo']
    mensaje = EmailMessage()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.set_content(cuerpo)
    
    # Enviar el correo electrónico utilizando SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(remitente, password)
        smtp.send_message(mensaje)