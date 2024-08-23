import speech_recognition as sr
import os
import pathlib

r = sr.Recognizer()

from pydub import AudioSegment

def convert_m4a_to_wav(m4a_file, wav_file):
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(wav_file, format="wav")

neuFolder = ('/Users/aniyataneja/Downloads/NPR Data/uploaded_files')

'''for filename in os.scandir(neuFolder):
    
    if filename.is_dir():
        thisFile = filename
        
        for x in os.scandir(thisFile):
            
            if x.is_file():
                file_extension = pathlib.Path(x).suffix
                
                if file_extension == '.m4a':
                    m4a_file = x.path
                    wav_file = x.path
                    convert_m4a_to_wav(m4a_file, wav_file)
                    neu = sr.AudioFile(x.path)
                    with neu as source:
                        audio = r.record(source)
                    print(r.recognize_google(audio))
                    
                else:
                    neu = sr.AudioFile(x.path)
                    with neu as source:
                        audio = r.record(source)
                    print(r.recognize_google(audio))'''

possibleError = False

for filename in os.scandir(neuFolder):
    
    if filename.is_dir():
        thisFile = filename
        
        for x in os.scandir(thisFile):
            
            if x.is_file():
                file_extension = pathlib.Path(x).suffix
                
                if file_extension == '.m4a' or file_extension == '.wav':
                    replacement_file = AudioSegment.empty()
                    m4a_file = x.path
                    replacement_file = thisFile.path
                    audio = AudioSegment.from_file(m4a_file)
                    audio.export(replacement_file, format="wav")
                    
                    '''m4a_file = x.path
                    wav_file = x.path
                    convert_m4a_to_wav(m4a_file, wav_file)'''
                    neu = sr.AudioFile(x.path)
                    with neu as source:
                        audio = r.record(source)
                    print(filename)
                    try:
                        print(r.recognize_google(audio))
                    except LookupError:
                        possibleError = True

                    if possibleError == True and file_extension == '.m4a':
                        m4a_file = x.path
                        wav_file = x.path
                        convert_m4a_to_wav(m4a_file, wav_file)
                        neu = sr.AudioFile(x.path)
                        with neu as source:
                            audio = r.record(source)
                        print(r.recognize_google(audio))


'''for index, item in enumerate(neuFolder, start = 0):
    for filename in os.scandir(neuFolder):
        if filename.is_dir():
            thisFile = filename
            for x in os.scandir(thisFile):
                if x.is_file():
                    file_extension = pathlib.Path(x).suffix
                    if file_extension == '.m4a':
                        m4a_file = x.path
                        wav_file = x.path
                        convert_m4a_to_wav(m4a_file, wav_file)
                        neu = sr.AudioFile(x.path)
                        with neu as source:
                            audio = r.record(source)
                        print(r.recognize_google(audio))
                    else:
                        neu = sr.AudioFile(x.path)
                        with neu as source:
                            audio = r.record(source)
                        print(r.recognize_google(audio))'''
