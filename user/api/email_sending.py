import smtplib
import requests
import email_details


def send_data(email, city, name_of_receiver):
    MY_EMAIL = email_details.email
    MY_PASSWORD = email_details.pass
    API_KEY = email_details.api_key
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
            msg=f"Subject: Hi, {name_of_receiver}, interested in our Services\n\nTemperature = {temperature}."
        )
