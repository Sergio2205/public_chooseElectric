import time
import openai
import requests
from openai import OpenAI

openai = OpenAI(api_key='Insert OpenAI API KEY')
TOKEN = "insert Telegram BOT TOKEN"

def get_updates(offset):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response

def get_openai_response(prompt):
    system = '''
       You are a personal assistant that helps the user make the decision to change their vehicle to an electric one.
        '''
    response = openai.chat.completions.create(
		model='ft:gpt-4o-mini-2024-07-18:personal:chooseelectric:ApIrUrZq',
		messages=[
            {"role": "system", "content" :f'{system}'},
            {"role": "user", "content" : 'I have a Audio A8 2020 and drive aproximatly 700km per month'},
            {"role": "assistant", "content" : f'''The Audi A8 2020 has an average fuel consumption of 8 liters per 100 km. 
             With your monthly commute of 4500 km, you would spend approximately 360 liters of gasoline per month. With the average price of 
             gasoline in Germany at €1.8 per liter, you would spend about €648 per month on gasoline.
             As an alternative, you could consider the Mercedes-Benz EQS, which is an all-electric vehicle. The EQS has an average consumption of 
             about 20 kWh per 100 km. For your monthly commute of 4500 km, you would consume about 900 kWh per month. With the average 
             electricity price in Germany at €0.3 per kWh, you would spend approximately €270 per month on electricity.

             This represents a saving of 378 euros per month, which equates to 58.33% savings compared to your current gasoline expenditure. 
             Annually, this translates into a savings of approximately 4536 euros. 

             I share with you the link to the Mercedes-Benz EQS so you can get more information: [Mercedes-Benz EQS](https://www.mercedes-benz.de/passengercars/models/saloon/eqs/overview.html).'''},
            {"role": "user", "content" : f'{prompt}'}],
		max_tokens=300,
		n=1,
		temperature=0)    
    return response.choices[0].message.content.strip()

def main():
    first_text = '''
    Greetings, I'm "chooseElectric." You can rely on me to advise you on whether purchasing an electric vehicle 
    will enhance your mobility and help the environment simultaneously. I would first like to know the model of your actual
      car as well as the approximate number of kilometers you drive each month.
'''
    offset = 0
    updates = get_updates(offset)
    if updates:
        chat_id = updates[0]["message"]["chat"]['id']
        send_messages(chat_id, first_text)
        offset = updates[0]["update_id"] +1
    while True:
        updates = get_updates(offset)
        if updates :
            for update in updates:
                offset = update["update_id"] +1
                chat_id = update["message"]["chat"]['id']
                user_message = update["message"]["text"]
                print(f"Received message: {user_message}")
                GPT = get_openai_response(user_message)
                send_messages(chat_id, GPT)
        else:
            time.sleep(1)

if __name__ == '__main__':
    main()
