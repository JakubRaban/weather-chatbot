from datetime import date
from random import choice

from witai import get_wit_response, parse
from chatreplies import *
import weather

print('Hello, weather chatbot here! What would you like to know about weather?')
while True:
    try:
        question = input()
        response = get_wit_response(question)
        data = parse(response)
        intent = data['intent']
        request_date = data['date']
        location = data['location']

        if not intent:
            print(choice(error_not_understood))

        elif intent == 'greetings':
            print(choice(greetings))

        elif intent == 'bye':
            print(choice(byes))
            break

        elif intent == 'joke':
            print(choice(jokes))

        elif intent == 'thanks':
            print(choice(youre_welcome))

        elif intent in ['weather_get', 'temperature_get', 'is_condition']:
            if not location:
                print(choice(error_no_location))
                continue
            request_condition = data['conditions']
            date_diff = (request_date - date.today()).days if request_date else 0
            if date_diff == 0:
                weather_conditions = weather.get_current_weather(location)
            elif 0 < date_diff < 3:
                weather_conditions = weather.get_forecast(location, date_diff)
            elif date_diff > 3:
                print(choice(error_date_too_late))
                continue
            else:
                print(choice(error_past_date))
                continue
            if intent == 'weather_get':
                print(f'In {location[0]} it {"will be" if date_diff else "is"} {weather_conditions["condition"]}'
                      f' and the temperature {"will be" if date_diff else "is"} {weather_conditions["temperature"]} '
                      f'degrees Celsius')
            elif intent == 'temperature_get':
                print(f'In {location[0]} the temperature {"will be" if date_diff else "is"} '
                      f'{weather_conditions["temperature"]} degrees Celsius')
            elif intent == 'is_condition':
                match = request_condition.lower() in weather_conditions['condition']
                print(f"{'Yes' if match else 'No'}, in {location[0]} it {'is' if not date_diff else 'will be'} "
                      f"{weather_conditions['condition']}")
    except:
        print(choice(error_not_understood))
