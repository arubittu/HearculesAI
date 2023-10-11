import torch
from transformers import pipeline
#from datasets import load_dataset

pipe = pipeline(
  "automatic-speech-recognition",
  model="openai/whisper-tiny",
  chunk_length_s=30,
  device=torch.device("mps"),
)

#ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
#sample = ds[0]["audio"]

prediction = pipe('audio.mp3',batch_size=8,return_timestamps=True)["chunks"]
print(prediction)
# we can also return timestamps for the predictions
#prediction = pipe(sample, return_timestamps=True)["chunks"]