# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted, ActionExecuted, EventType

class ActionSessionStart(Action):
    def name(self) -> str:
        return "action_session_start"

    async def run(self, dispatcher, tracker, domain):
        # Aquí va tu lógica personalizada
        # Ejemplo: enviar un mensaje de bienvenida
        dispatcher.utter_message("¡Hola! Bienvenido al chatbot.")

        return [SessionStarted(), ActionExecuted("action_listen")]
