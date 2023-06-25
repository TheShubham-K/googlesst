import google 
from google.cloud import speech
import subprocess
import io

# Set up the Google Cloud Speech-to-Text client
client = speech.SpeechClient()

# Set up the subprocess to capture the audio stream
command = ['parec', '--format=s16le', '--rate=44100', '--channels=1', '--device=6']
process = subprocess.Popen(command, stdout=subprocess.PIPE)

# Create a recognition config
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-US'
)

# Create an audio source from the subprocess stdout
audio_source = speech.RecognitionAudio(uri='stdout')

# Create a speech recognition request
request = speech.RecognizeRequest(config=config, audio=audio_source)

# Perform the speech recognition
response = client.recognize(request=request)

# Process the response
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

# Close the subprocess
process.terminate()
