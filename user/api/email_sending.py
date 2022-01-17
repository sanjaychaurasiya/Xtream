import smtplib
import requests


def send_data(email, city, name_of_receiver):
    MY_EMAIL = 'smtptesting404@gmail.com'
    MY_PASSWORD = 'smtp@404'
    API_KEY = 'e9e142930405697e087dedc3c33b0ff2'
    API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
    TO_EMAIL = email
    City_Name = city

    response = requests.get(url=API_ENDPOINT, params={'q': City_Name, 'appid': API_KEY})
    response.raise_for_status()
    data = response.json()
    temperature = data['main']['temp']

    with smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )
        smtp.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Hi, {name_of_receiver}, interested in our Services\n\nTemperature = {temperature}. <p>&#128512;</p>"
        )
