# Python Program that helps translate Speech to Text
 
import speech_recognition


# The Recognizer is initialized.
UserVoiceRecognizer = speech_recognition.Recognizer()
 
while(True):
    try:
        with speech_recognition.Microphone() as UserVoiceInputSource:
 
            # UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.05)
 
            # The Program listens to the user voice input.
            
            UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource,timeout=0.25)
            
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
            print(UserVoiceInput_converted_to_Text)
            
    except KeyboardInterrupt:
        print('A KeyboardInterrupt encountered; Terminating the Program.')
        exit(0)
    
    except Exception as e:
        pass