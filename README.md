# AI Voice Assistant

An interactive voice assistant powered by OpenAI's Whisper model and LangChain's LLM system. It allows users to engage in a dynamic conversation with the AI using natural language.

## Features

- **Real-time Speech-to-Text (STT)**: Transcribe user's spoken words into text.
- **AI Response Generation**: Leverage OpenAI and LangChain's LLM to generate conversational responses.
- **Real-time Text-to-Speech (TTS)**: Convert AI-generated text responses into speech for auditory feedback.

## Installation

1. Clone the repository:
```
git clone <repository-url>
```
2. Navigate to the repository directory and install the required packages:
```
cd <repository-name>
pip install -r requirements.txt
```

## Usage

Run the voice assistant with:
```
python orchestrate.py
```
Follow the prompts to interact with the AI. Speak your queries, and the assistant will respond audibly.

## Dependencies

- pyaudio
- SpeechRecognition
- torch (with CUDA 11.6 support)
- whisper (from OpenAI's GitHub repository)
- openai
- langchain
- websockets
- numpy

## Contribution

Contributions are welcome! Please make sure to test your code thoroughly before submitting a pull request.

## License

This project is licensed under the MIT License.
