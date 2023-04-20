import pandas as pd
import smtplib
from email.message import EmailMessage
from datetime import datetime

class EnviarMail:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def enviar_correos(self, datos, asunto, cuerpo_html):
        # Configuramos los parámetros del asuario y los datos
        remitente = self.email

        # Establecemos la conexión con el servidor de correo usando protocolo smtp
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(self.email, self.password)
            
            # Filtramos los datos para que sólamente se envíen los correos a las personas que cumplen años en el día de hoy
            hoy = datetime.now().strftime('%d/%m')
            datos_hoy = datos[datos['cumpleaños'].apply(lambda x: datetime.strptime(f"{datetime.now().year}/{x[-2:]}/{x[:5]}", '%Y/%y/%d/%m').strftime('%d/%m') == datetime.now().strftime('%d/%m'))]



            # Recorremos el DataFrame con un ciclo for y enviamos un correo electrónico a cada destinatario
            for i, fila in datos_hoy.iterrows():
                destinatario = fila['correo']
                mensaje = EmailMessage()
                mensaje['From'] = remitente
                mensaje['To'] = destinatario
                mensaje['Subject'] = asunto
                mensaje.set_content(cuerpo_html, subtype='html')
                servidor.send_message(mensaje)

# Importamos los datos y los guardamos en un variable
datos = pd.read_csv('datos.csv')

# Creamos la instancia de la clase EnviarMail
enviar_mail = EnviarMail('mercado.isaacpablor@gmail.com', 'caahdydzivvgikqf')

# Enviamos el correo electrónico con formato HTML
asunto = 'Feliz Cumpleaños, crack'
cuerpo_html = """
<html>
  <head>
    <meta charset="utf-8">
    <title>Feliz Cumpleaños</title>
  </head>
  <body>
    <div style="text-align: center;">
      <h1>¡Feliz Cumpleaños!</h1>   
      <p>¡Que tengas un día lleno de amor, alegría y muchos regalos!</p>
      <p> Sabés que sos super groso y en esta empresa te queremos un montón!</p>
      <img src="https://github.com/primercado/reto_3_correos/blob/master/Sin%20t%C3%ADtulo.jpeg?raw=true" alt="Descripción de la imagen">
    </div>
  </body>
</html>
"""
enviar_mail.enviar_correos(datos, asunto, cuerpo_html)


print ('El correo fué enviado con éxito')
