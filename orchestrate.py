from stt import *
from tts import *
import threading
import time
import os
os.environ["OPENAI_API_KEY"] = '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'
chat_history = [{'role': 'system', 'content': """you are receptionist at taj hotel mumbai.
                                    answer user queries in a friendly style in a very short manner."""}] # pass as message

speaker_flag = False
def mic_thread():
    print("SPEAK")
    transcription = transcribe(speaker_event) # returns a list
    return

def speaker_thread():
    if speaker_flag:
        print("AI TALKING")
        ai_response = asyncio.run(chat_completion(chat_history))
        chat_history.append({'role': 'assistant', 'content': ai_response})
    else:
        time.sleep(1)

    print("AI STOPPED TALKING")
    return


# test 
if __name__ == "__main__":
    # chat_history = [{'role': 'system', 'content': """you are receptionist at taj hotel mumbai.
    #                                 answer user queries in a friendly style in a very short manner."""}] # pass as message
    
    mic_event = threading.Event()
    speaker_event = threading.Event()

    mic_thread = threading.Thread(target=mic_thread, args=())
    speaker_thread = threading.Thread(target=speaker_thread, args=())

    mic_thread.start()
    speaker_thread.start()

    mic_thread.join()
    speaker_thread.join()
