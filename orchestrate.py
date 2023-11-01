from stt import *
from tts import *
import threading
import time


def mic_thread(mic_event, speaker_event, chat_history):
    
    while True:
        try:
            print("SPEAK")
            transcription = transcribe(speaker_event) # returns a list
            print("Microphone: Voice input received")
            user_query_str = ' '.join(transcription)
            chat_history.append({'role': 'user', 'content': user_query_str})
            speaker_event.set()
            mic_event.set()
            
        except KeyboardInterrupt:
            break
     
    return

def speaker_thread(mic_event, speaker_event, chat_history):
    while True:
        try:
            mic_event.wait() 
            if speaker_event.is_set():
                print("AI TALKING")
                ai_response = asyncio.run(chat_completion(chat_history))
                chat_history.append({'role': 'assistant', 'content': ai_response})
                speaker_event.clear()
                mic_event.clear()
            else:
                time.sleep(1)

        except KeyboardInterrupt:
            break
        print("AI STOPPED TALKING")
    return


# test 
if __name__ == "__main__":
    chat_history = [{'role': 'system', 'content': """you are receptionist at taj hotel mumbai.
                                    answer user queries in a friendly style in a very short manner."""}] # pass as message
    
    mic_event = threading.Event()
    speaker_event = threading.Event()

    mic_thread = threading.Thread(target=mic_thread, args=(mic_event, speaker_event, chat_history))
    speaker_thread = threading.Thread(target=speaker_thread, args=(mic_event, speaker_event, chat_history))

    mic_thread.start()
    speaker_thread.start()

    mic_thread.join()
    speaker_thread.join()
