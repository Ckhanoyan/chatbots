import nltk
from nltk.chat.util import Chat, reflections
import requests

# Weather function to fetch data from OpenWeatherMap API
def get_weather(city):
    api_key = '719327cf0d486be8dd9d5795a399b649'
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Complete URL
    url = f"{base_url}q={city}&appid={api_key}&units=metric"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather = data['weather'][0]['description']

        # Return a formatted weather response
        return f"The weather in {city} is {weather} with a temperature of {temperature}°C and humidity of {humidity}%"
    else:
        return "Sorry, I couldn't fetch the weather data at the moment."

# Define the chatbot's responses and patterns
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey! How can I help you today?']),
    (r'how are you?', ['I am doing great, thank you!', 'I am fine, how about you?']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
    (r'what is your name?', ['I am a chatbot, I don\'t have a name yet!']),
    (r'weather in (.*)', ['%1']),  # Placeholder for weather response
    (r'(.*)', ['Sorry, I didn\'t understand that. Can you rephrase?'])  # Fallback for unknown input
]

# Create the chatbot object
chatbot = Chat(patterns, reflections)

# Start the conversation
def start_chat():
    print("Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye!")
            break
        else:
            if 'weather in' in user_input.lower():
                city = user_input.split('weather in ')[1]
                response = get_weather(city)
            else:
                response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
