from twilio.rest import Client
import requests

account_sid = 'ACxxx'
auth_token = 'xxxx'

client = Client(account_sid, auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']

Message = 'Hi abc, Want to listen a fun fact? Number of people in space right now is '+str(number_iss)+str(people['people'])
message = client.messages.create(
    to="+91xxx",
    from_="+xxx",
    body=Message)

print(message.sid)
