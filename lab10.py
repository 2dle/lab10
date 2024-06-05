import requests
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    Alice = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите...")
        Alice.adjust_for_ambient_noise(source)
        audio = Alice.listen(source)
    try:
        word = Alice.recognize_google(audio, language='ru-RU')
        print(f"Вы сказали: {word}")
        return word
    except Exception as e:
        print(e)
        return None

def create_user():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        user_data = response.json()['results'][0]
        user_name = f"{user_data['name']['first']} {user_data['name']['last']}"
        speak(f"Пользователь {user_name} создан.")
    else:
        speak("Ошибка при создании пользователя.")
def hour_fifteen():
    engine.say("Вёл Моисей евреев по пустыне сорок лет и час 15, довёл, а его спрашивают: Моисей, ты зачем нас вёл сорок лет? Тут же идти всего час 15. А он им и отвечает: Я закреплял")
    engine.runAndWait()
    
def get_name():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        user_data = response.json()['results'][0]
        user_name = f"{user_data['name']['first']} {user_data['name']['last']}"
        speak(f"Имя пользователя: {user_name}.")
    else:
        speak("Ошибка при получении имени.")

def get_country():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        user_data = response.json()['results'][0]
        country = user_data['location']['country']
        speak(f"Страна пользователя: {country}.")
    else:
        speak("Ошибка при получении страны.")

def create_form():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    name = data["results"][0]["name"]["first"]
    gender = data["results"][0]["gender"]
    dob = data["results"][0]["dob"]["date"]
    email = data["results"][0]["email"]
    survey = f"Юмя: {name}, Пол: {gender}, Дата рождения: {dob}, Email: {email}"
    engine.say("Анкета сохранена")
    engine.say(survey)
    engine.runAndWait()

def save_photo():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    photo_url = data["results"][0]["picture"]["large"]
    with open("user_photo.jpg", "wb") as f:
        f.write(requests.get(photo_url).content)
    engine.say("Фотография сохранена")
    engine.runAndWait()

def main():
    speak("Привет! Я ваш голосовой ассистент. Чем могу помочь?")
    while True:
        command = recognize_speech()
        if command:
            if "создать" in command:
                create_user()
            elif "имя" in command:
                get_name()
            elif "страна" in command:
                get_country()
            elif "анкета" in command:
                create_form()
            elif "сохранить" in command:
                save_photo()
            elif "1:15" in command:
                hour_fifteen()
            else:
                speak("Не распознана команда. Пожалуйста, повторите.")
        else:
            speak("Ошибка в запросе. Пожалуйста, повторите.")

if __name__ == "__main__":
    main()