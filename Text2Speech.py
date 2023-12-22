from gtts import gTTS
import pygame
import io

def play_text_speech(text, lang='en'):
    # Generate the speech as an in-memory file
    speech = io.BytesIO()
    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(speech)
    speech.seek(0)

    # Initialize Pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(speech)

    # Play the speech
    pygame.mixer.music.play()
    
    # Wait for the speech to finish
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(100)

# Example usage



