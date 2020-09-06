import requests
from datetime import datetime

url = 'http://api.weatherapi.com/v1'
key = 'd90d5174e28a4b8a9a093053201205'


def get_current_weather(location):
    params = {'key': key, 'q': f'{location[1]},{location[2]}'}
    r = requests.get(url + '/current.json', params=params)
    response = r.json()
    return {
        'temperature': response['current']['temp_c'],
        'condition': response['current']['condition']['text'].lower()
    }


def get_forecast(location, days_ahead):
    params = {'key': key,
              'q': f'{location[1]},{location[2]}',
              'days': days_ahead + 1
              }
    r = requests.get(url + '/forecast.json', params=params)
    response = r.json()
    forecast_day = response['forecast']['forecastday'][days_ahead]['day']
    return {
        'temperature': forecast_day['maxtemp_c'],
        'condition': forecast_day['condition']['text'].lower()
    }
