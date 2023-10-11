from stt import *
from tts import *

def run():
    chat_history = [{'role': 'system', 'content': """you are receptionist at taj hotel mumbai.
                                    answer user queries in a friendly style in a very short manner."""}] # pass as message
    while True:
        try:
            print("SPEAK")
            transcription = transcribe() # returns a list
            user_query_str = ' '.join(transcription)
            chat_history.append({'role': 'user', 'content': user_query_str})
            
            print("AI TALKING")
            ai_response = asyncio.run(chat_completion(chat_history))
            chat_history.append({'role': 'assistant', 'content': ai_response})
            
            print("AI STOPPED TALKING") 
            
            #sleep(0.1)
        except KeyboardInterrupt:
            break
     
    return


# test 
if __name__ == "__main__":
    run()