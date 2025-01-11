import speechrec
import texttospeech
import datetime
import webbrowser
def action(data):
    user_data=data.lower()
    if "what is your name" in user_data:
        texttospeech.text_to_speech("my name is FELIX, i am designed to assist you")
        return "my name is FELIX, i am designed to assist you"
    elif "hello" or "hi" or "namaste" in user_data:
        texttospeech.text_to_speech("hey, how can I help you")
        return "hey, how can I help you"
    elif "good morning" in user_data:
        texttospeech.text_to_speech("good morning, have a great day ahead")
        return "good morning, have a great day ahead"
    elif "time now" in user_data:
        current_time=datetime.datetime.now()
        time=(str)(current_time)+"hour:",(current_time.minute)+"minutes"
        texttospeech.text_to_speech(time)
        return time
    elif "shutdown" in user_data:
        texttospeech.text_to_speech("okay")
        return "okay"
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        texttospeech.text_to_speech("opening spotify.com")
        return "opening spotify.com"
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        texttospeech.text_to_speech("opening youtube")
        return "opening youtube"
    elif "gen-z didi youtube" in user_data:
        webbrowser.open("https://www.youtube.com/results?search_query=the+genz+didi")
    elif "open youtube music" in user_data:
        webbrowser.open("https://music.youtube.com/")
    elif "google" in user_data:
        webbrowser.open("https://www.google.com/")
        texttospeech.text_to_speech("opened google")
        return "opened google"
    else:
        texttospeech.text_to_speech("pardon, i couldn't understand")
        return "pardon, i couldn't understand"

