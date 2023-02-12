import speech_recognition as sr
import pyttsx3
import re
r=sr.Recognizer()

def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def Amount(text):
    amountList=re.findall(r'\d+',text)
    print(amountList)
    amountInt=int(amountList[0])
    print(amountInt)
    return amountInt

def EnableVoiceCommand():
    try:
        with sr.Microphone() as source:
            SpeakText("Do you want to enable voice command?")
            r.adjust_for_ambient_noise(source,duration=0.2)
            audio=r.listen(source)
            AnsInText=r.recognize_google(audio)
            print(AnsInText)
            print(type(AnsInText))
            return AnsInText
    except sr.RequestError as e:
        print(e)
    except sr.UnknownValueError as e:
        print(e)

def VoiceCommands():
    try:
        with sr.Microphone() as source1:
            r.adjust_for_ambient_noise(source1,duration=0.2)
            audio=r.listen(source1)
            AudioInText=r.recognize_google(audio)
            rs=str(Amount(AudioInText))
            SpeakText(rs+"Added")
    except sr.RequestError as e:
        print(e)
    except sr.UnknownValueError as e:
        print(e)

if __name__=="__main__":
    Ans=EnableVoiceCommand()#Error Ans=NONE Convert To Str
    print("Ans is "+Ans)
    if Ans.lower()=="yes":
        VoiceCommands()
    else:
        SpeakText("Voice Command Deactived")
