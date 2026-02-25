# from chat.urls import ask_question
from chat.utils import get_answer

response = get_answer("What is computer programming?")
print(response)