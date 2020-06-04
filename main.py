import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

#Convert text to Speech

def textToSpeech(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

#It will return pydub audio segments

def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined
#Make segments of Original Audio

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    #For Hindi Announcement

    # 1- Generating Wishing Announcement
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_Announcement.mp3",format="mp3")

    # 2- Generating City Name 1 (From City)


    # 3- Middle Connection
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_Announcement.mp3", format="mp3")

    # 4- Via City

    # 5- Middle Connection 2
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_Announcement.mp3", format="mp3")

    # 6- Generating City Name (To-City)

    # 7- Going Announcement
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_Announcement.mp3", format="mp3")

    # 8- Train no and name

    # 9- Generate time name
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_Announcement.mp3", format="mp3")

    # 10- Platform Number

    # 11- Going to Come
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_Announcement.mp3", format="mp3")

# def generateSkeleton_English():
#     audio_eng = AudioSegment.from_mp3('railway.mp3')
#
#     #For English Announcement
#
#     # 1- Generating Wishing Announcement
#     start = 19000
#     finish = 22200
#     audioProcessed_eng = audio_eng[start:finish]
#     audioProcessed_eng.export("1_Announcement_Eng.mp3",format="mp3")
#
#     # 2- Generating City Name 1 (From City)
#
#
#     # 3- Middle Connection
#     start = 31000
#     finish = 32000
#     audioProcessed_eng = audio_eng[start:finish]
#     audioProcessed_eng.export("3_Announcement_Eng.mp3", format="mp3")
#
#     # 4- Via City
#
#     # 5- Middle Connection 2
#     start = 35000
#     finish = 36000
#     audioProcessed_eng = audio_eng[start:finish]
#     audioProcessed_eng.export("5_Announcement_Eng.mp3", format="mp3")
#
#     # 6- Generating City Name (To-City)
#
#     # 7- Going Announcement
#     start = 33000
#     finish = 34000
#     audioProcessed_eng = audio_eng[start:finish]
#     audioProcessed_eng.export("7_Announcement_Eng.mp3", format="mp3")
#
#     # 8- Train no and name
#
#     # 9- Generate time name
#     start = 105500
#     finish = 108200
#     audioProcessed_eng = audio_eng[start:finish]
#     audioProcessed_eng.export("9_Announcement_Eng.mp3", format="mp3")
#
#     # 10- Platform Number
#
#     # 11- Going to Come
#     start = 39000
#     finish = 41000
#     audioProcessed_eng = audio_eng[start:finish]
#     audioProcessed_eng.export("11_Announcement_Eng.mp3", format="mp3")

# Takes csv file of the announcements

def generateAnnouncement(filename):
     df= pd.read_excel(filename)

     for index,item in df.iterrows():
     # From City
         textToSpeech(item['from'],'2_Announcement.mp3')
         # Via City
         textToSpeech(item['via'], '4_Announcement.mp3')
         # To City
         textToSpeech(item['to'], '6_Announcement.mp3')
         # Train Number
         textToSpeech(item['train_no']+" "+item['train_name'], '8_Announcement.mp3')
         # Platform Number
         textToSpeech(item['platform'], '10_Announcement.mp3')

         audios = [f"{i}_Announcement.mp3" for i in range(1,12)]

         announcement = mergeAudios(audios)
         announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")


if __name__ == '__main__':
    print("Generate Skeleton...")
    generateSkeleton()
    print("Now Generating Announcements...")
    # print("ENG")
    # generateSkeleton_English()
    generateAnnouncement("announce_hindi.xlsx")
