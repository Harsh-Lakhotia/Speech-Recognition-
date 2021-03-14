import speech_recognition as sr
import webbrowser

import pyttsx3
import os



#offline text to speech
def SpeakText(command):#speak and repeat

    # Initialize the engine
    engine = pyttsx3.init()

    newVoiceRate = 120
    engine.setProperty('rate', newVoiceRate)

    engine.say(command)
    engine.runAndWait()

r= sr.Recognizer()
while True:

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        print("OPTIONS:\n 1.Convert Speech to text\n2.Search on web using wikipedia\n3.Search music on YOUTUBE\n")
        print("Say something!")
        audio = r.listen(source)
        print("You said "+ r.recognize_google(audio))

    words = r.recognize_google(audio)

    if "convert" in words:


        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("\nConverting speech to text")
            print("Speak now :")
            audio = r.listen(source)

        try:
            result = r.recognize_google(audio)
            print("You said \n" + result)
        except Exception as e:
            print(e)






    if "web" in words:


        url = 'https://www.wikipedia.org/wiki/'
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("\nSearching on WIKIPEDIA\nPlease State the search_query  :")
            audio = r.listen(source)

            try:
                get = r.recognize_google(audio)
                print("u said: \n" + get)
                webbrowser.open_new(url+get)
            except sr.UnknownValueError:
                print("Sorry Could't understand Audio")
            except sr.RequestError :
                print("Failed to retrieve results")






    if "music" in words:

        url2 = 'https://www.youtube.com/results?search_query='

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("\nSearching on Music \n Please State the search_query :")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print("You said :\n" + text)
                webbrowser.open_new(url2 + text)
            except sr.UnknownValueError:
                print("Sorry Could't understand Audio")
            except sr.RequestError :
                print("Failed to retrieve results")


    if "speak" in words:# 1

        f = open("read.txt", "r")
        SpeakText(f.read())
        print(f.read())



    if "record" in words:  # 2 3

        # obtain audio form the microphone
        r = sr.Recognizer()  # we can remore this experiment
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Recording speech")
            print("Speak now :")
            audio = r.listen(source)
        # recognize speech using Google
        try:
            with open("record.wav", "wb") as f:  # 2 3
                f.write(audio.get_wav_data())

        except Exception as e:
            print(e)


    if "play" in words:

        try:

            os.system("record.wav")
        except Exception as e:
            print(e)



    if "open" in words:
        import webbrowser as wb
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Which website you want to open!")
            audio = r.listen(source)
            print("Got it! Now to recognize it...")
            # recognize speech using Google
            try:
                text = r.recognize_google(audio)
                print("You said: \n " + text)
                wb.get(chrome_path).open(text)
            except Exception as e:
                print(e)

    if "repeat" in words:

        # obtain audio form the microphone
        r = sr.Recognizer()  # we can remore this experiment
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Converting speech to text")
            print("Speak now :")
            audio = r.listen(source)
        # recognize speech using Google
        try:
            result = r.recognize_google(audio)
            print("You said \n" + result)
            SpeakText(result)

        except Exception as e:
            print(e)

    if "calculator" in words:  # 9
        import subprocess

        print("hi")
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    if "audio to file" in words:  # 6

        r = sr.Recognizer()
        # define the audio file
        # audio_file = sr.AudioFile('microphone-results.wav')
        # speech recognition
        # with audio_file as source:
        with    sr.AudioFile('record.wav') as source:
            audio = r.record(source)
        result = r.recognize_google(audio)
        # exporting the result
        with open('audiotofile.txt', mode='w') as file:
            file.write("Recognized text:")
            file.write("\n")
            file.write(result)
            print("converted to audio file !")

    if "turn off" in words:


        print("r u sure")

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                if "yes" in r.recognize_google(audio):
                    os.system("shutdown /s /t 1")
            except Exception as e:
                print(e)

    if "speech to text" in words:  #

        # obtain audio form the microphone
        r = sr.Recognizer()  # we can remore this experiment
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Converting speech to text")
            print("Speak now :")
            audio = r.listen(source)
        # recognize speech using Google
        try:
            result = r.recognize_google(audio)
            print("You said \n" + result)

            # exporting the result
            with open('test.txt', mode='w') as file:  # 10
                file.write("Recognized text:")
                file.write("\n")
                file.write(result)
                print("ready!")

        except Exception as e:
            print(e)

    if "file" in words:
        #os.startfile('decribe.docx')

        os.startfile('C:\\Users\\a\\Desktop\\Python.docx')

    if "3" in words:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Say something to make audio wav file ")
            audio = r.listen(source)
            print("Got it")

        try:
            print("you said " + r.recognize_google(audio))
            print("\n audio sucessfully recorded ! check file directory ")
        except Exception as e:
            print(e)

        with open("microphone-results1.wav", "wb") as f:
            f.write(audio.get_wav_data())

        with open("microphone-resukts1.aiff", "wb") as f:
            f.write(audio.get_aiff_data())

        with open("microphone-results1.flac", "wb") as f:
            f.write(audio.get_flac_data())

    print("\n\nDo you want to continue , say yes or no\n\n")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            if "no" in r.recognize_google(audio):
                break
        except Exception as e:
            print(e)
