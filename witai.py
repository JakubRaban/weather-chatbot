import json

from wit import Wit
from datetime import date

client = Wit('2J77PXYSX2M4ZG5OPIITFZ7IZ4HENFPZ')


def get_wit_response(text):
    return client.message(text)


def parse(wit_response):
    result = {'intent': None, 'location': None, 'date': None, 'conditions': None}
    entities = wit_response['entities']
    if 'intent' in entities and entities['intent'][0]['confidence'] > 0.7:
        result['intent'] = entities['intent'][0]['value']
    elif 'greetings' in entities and entities['greetings'][0]['confidence'] > 0.7:
        result['intent'] = 'greetings'
    elif 'bye' in entities and entities['bye'][0]['confidence'] > 0.7:
        result['intent'] = 'bye'
    elif 'thanks' in entities and entities['greetings'][0]['confidence'] > 0.7:
        result['intent'] = 'thanks'
    else:
        return result
    if 'location' in entities:
        location = entities['location'][0]['resolved']['values'][0]
        result['location'] = location['name'], location['coords']['lat'], location['coords']['long']
    if 'datetime' in entities:
        result['date'] = date.fromisoformat(entities['datetime'][0]['value'][:10])
    if 'conditions' in entities:
        result['conditions'] = entities['conditions'][0]['value']
    return result
