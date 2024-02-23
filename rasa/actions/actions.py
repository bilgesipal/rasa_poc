import os
from typing import Any, Text, Dict, List
import pandas as pd
import requests
import openai
from openai import OpenAI
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

os.environ['OPENAI_API_KEY'] = 'write your own key'

class RestaurantAPI(object):

    def __init__(self):
        self.db = pd.read_csv("restaurants.csv")

    def fetch_restaurants(self):
        print(self.db.head())
        return self.db.head()

    def format_restaurants(self, df, header=True) -> Text:
        return df.to_csv(index=False, header=header)


class ChatGPT(object):

    def __init__(self):

        self.client= OpenAI(api_key=os.environ['OPENAI_API_KEY'] )

        self.prompt = "Answer the following question, based on the data shown. " \
                      "Answer in a complete sentence and don't say anything else."

    def ask(self, restaurants, question):
        content = self.prompt + "\n\n" + restaurants + "\n\n" + question

        result = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user",
                       "content": content}],
            max_tokens=250
        )

        print('RESULT', result.choices[0].message.content)
        return result.choices[0].message.content

restaurant_api = RestaurantAPI()
chatGPT = ChatGPT()



class ActionShowRestaurants(Action):

    def name(self) -> Text:
        return "action_show_restaurants"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        restaurants = restaurant_api.fetch_restaurants()
        results = restaurant_api.format_restaurants(restaurants)
        readable = restaurant_api.format_restaurants(restaurants[['Restaurants', 'Rating']], header=False)
        dispatcher.utter_message(text=f"Here are some restaurants:\n\n{readable}")

        return [SlotSet("results", results)]


class ActionRestaurantsDetail(Action):
    def name(self) -> Text:
        return "action_restaurants_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        previous_results = tracker.get_slot("results")
        question = tracker.latest_message["text"]
        answer = chatGPT.ask(previous_results, question)
        dispatcher.utter_message(text = answer)
